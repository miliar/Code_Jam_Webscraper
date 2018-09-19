from functools import wraps
import sys


def parse_input(func=None, file_name=None):

    def actual_decorator(function):
        @wraps(function)
        def decorate(*args, **kwargs):
            fname = file_name
            if len(sys.argv) > 1:
                fname = sys.argv[1]
            if fname is not None:
                with open(fname, "r") as f:
                    t = int(f.readline())
                    function(f=f, t=t, *args, **kwargs)
            else:
                raise Exception("file name cannot be None")
        return decorate
    if func is None:
        return actual_decorator
    else:
        return actual_decorator(func)


def log_output(func=None, file_name=None):

    def actual_decorator(function):
        @wraps(function)
        def decorate(*args, **kwargs):
            if file_name is not None:
                fname = file_name
            else:
                fname = 'out.txt'
            with open(fname, "w") as f:
                sys.stdout = f
                function(*args, **kwargs)
        return decorate
    if func is None:
        return actual_decorator
    else:
        return actual_decorator(func)