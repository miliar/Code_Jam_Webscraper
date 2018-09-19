from datetime import datetime
from threading import current_thread
import time

__author__ = 'tehsphinx'


# def timeit(method):
#     def timed(*args, **kw):
#         ts = time.time()
#         result = method(*args, **kw)
#         te = time.time()
#
#         print('%r (%r, %r) %03d msec' % (method.__name__, args, kw, te - ts))
#         return result
#
#     return timed


def timeitloop(func=None, loops=1, verbose=False):
    if func is not None:
        def inner(*args, **kwargs):

            sums = 0.0
            mins = 1.7976931348623157e+308
            maxs = 0.0
            print('====%s Timing====' % func.__name__)
            result = None
            for i in range(0, loops):
                t0 = time.time()
                result = func(*args, **kwargs)
                dt = time.time() - t0
                mins = dt if dt < mins else mins
                maxs = dt if dt > maxs else maxs
                sums += dt
                if verbose:
                    print('\t%r ran in %2.9f sec on run %s' % (func.__name__, dt, i))
            print('%r min run time was %2.9f sec' % (func.__name__, mins))
            print('%r max run time was %2.9f sec' % (func.__name__, maxs))
            print('%r avg run time was %2.9f sec in %s runs' % (func.__name__, sums / loops, loops))
            print('==== end ====')
            return result

        return inner
    else:
        def partial_inner(f):
            return timeitloop(f, loops, verbose)

        return partial_inner


class dbg():
    BLACK = 30
    RED = 31
    GREEN = 32
    BROWN = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    DEFAULT = 39

    show_time = True
    show_thread = True

    def __init__(self, *args, **kwargs):
        if 'color' in kwargs:
            color = kwargs['color']
            del (kwargs['color'])
        else:
            color = self.DEFAULT

        prefix = []
        if self.show_time:
            prefix.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        if self.show_thread:
            prefix.append(current_thread().getName())
        if len(prefix) > 0:
            prefix.append('-- ')

        args = list(args)
        args += [{k: v} for k, v in kwargs.items()]

        print('\033[0;{0}m'.format(color), end='')
        print(*prefix, end='')
        print(*args, end='')
        print('\033[0;{0}m'.format(self.DEFAULT))


def dbg_err(*args, **kwargs):
    dbg(*args, color=dbg.RED, **kwargs)


def dbg_warn(*args, **kwargs):
    dbg(*args, color=dbg.BROWN, **kwargs)

