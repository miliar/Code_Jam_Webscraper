from functools import wraps
import time
import os

###############################
##      useful decorators
###############################

def memoize_it(inner_func):
    # a decorator for memoizing function outputs
    global __memoization_registry
    try:
        __memoization_registry
    except NameError:
        __memoization_registry = []
    cache = {}
    __memoization_registry.append(cache)
    @wraps(inner_func)
    def wrap(*args):
        if args not in cache:
            cache[args] = inner_func(*args)
        return cache[args]
    return wrap

def reset_memoization ():
    # clear all previous memoization. For use in the beginning of a new test-case
    global __memoization_registry
    try:
        for cache_d in __memoization_registry:
            cache_d.clear()
    except NameError:
        pass
        
def time_it(inner_func):
    # a decorator for adding printing of timing for a function
    @wraps(inner_func)
    def wrap(*args):
        print ('--> Start function \'' + inner_func.__qualname__ + '\' : ', time.ctime())
        starttime = time.time()
        res = inner_func(*args)
        endtime = time.time()
        print ('--> End   function \'' + inner_func.__qualname__ + '\' : ', time.ctime())
        print ('--> Elapsed time \'' + inner_func.__qualname__ + '\' : ', endtime-starttime)
        print()
        return res
    return wrap
    
def count_it (inner_func):
    # a decorator for counting the number of calls to the wrapped function
    global _CALL_FUNC_COUNTERS
    if '_CALL_FUNC_COUNTERS' not in globals():
        _CALL_FUNC_COUNTERS = {}
    assert type(_CALL_FUNC_COUNTERS) == dict
    assert inner_func.__qualname__ not in _CALL_FUNC_COUNTERS
    _CALL_FUNC_COUNTERS[inner_func.__qualname__] = 0
    @wraps(inner_func)
    def wrap(*args):
        global _CALL_FUNC_COUNTERS
        _CALL_FUNC_COUNTERS[inner_func.__qualname__] += 1
        return inner_func(*args)
    return wrap

def pre_process_it (inner_func):
    # a decorator for pre-processing the function and automatically save the result 
    import inspect
    import pickle
    a = inspect.getargspec(inner_func)
    if a.args or a.keywords or a.varargs or a.defaults:
        raise ValueError ('A pre process function must not have arguments')        
    
    @time_it
    @wraps(inner_func)
    def wrap (*args):
        filename = 'preprocess_' + inner_func.__qualname__ + '.pickle'
        if not filename in os.listdir():
            print ('--> Pre process started for function \'' + inner_func.__qualname__ + '\' ....')
            preProcessData = inner_func()
            print ('--> Pre process ended for function \'' + inner_func.__qualname__ + '\'')
            print ('--> Pickling started for function \'' + inner_func.__qualname__ + '\' ....')
            with open(filename, 'wb') as f_pp:
                pickle.dump(preProcessData, f_pp, pickle.HIGHEST_PROTOCOL)
            print ('--> Pickling ended for function \'' + inner_func.__qualname__ + '\'')
        print ('--> Unpickling pre-processed data of function \'' + inner_func.__qualname__ + '\' ...')
        with open(filename, 'rb') as f_pp:
            data = pickle.load(f_pp)
        print ('--> Unpickling ended')
        print()
        return data

    return wrap
 

        

###########################################
# write code here
###########################################
import itertools



def count_moves(A, p):
    copy_A = A[:]
    res = 0
    for i in p:
        res += copy_A.index(i)
        copy_A.remove(i)
    return res
        
    
def is_legal (p):
    mx = max(p)
    ind = p.index(mx)
    for i in range(ind):
        if p[i] > p[i+1]:
            return False
    for i in range(ind, len(p)-1):
        if p[i] < p[i+1]:
            return False
    return True


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))


@time_it
def solve (f_in, f_out):
    T = int(f_in.readline())
    for testcase in range(1, T+1):
        print (testcase)
        N = int(f_in.readline())
        A = [int(x) for x in f_in.readline().split()]
        #mx = max(A)
        assert N  == len(A)
        best_choice = 10**80
        for subset1 in powerset(A):
            subset2 = set(A).difference(subset1)
            arranged = list(sorted(subset1)) + list(sorted(subset2,reverse=True))
            assert len(arranged) == len(A)
            if is_legal(arranged):
                m  =  count_moves(A, arranged)
                #print(A, p, m)
                best_choice = min(best_choice, m)
        
        f_out.write('Case #' + str(testcase) + ': ' + str(best_choice) + '\n')
        print()





###########################################
# automatic runner
###########################################

@time_it
def main_run():
    print ('Directory : ', os.getcwd())
    filenames = [x for x in os.listdir ()]
    filenames = [x for x in filenames if x.endswith('.in')]
    l1 = [(os.stat(x).st_mtime, x) for x in filenames]
    if not l1:
        raise ValueError('No input file found')
    chosen_filename =  sorted(l1)[-1][1][:-3]
    print ('Chosen Filename : ',chosen_filename)
    print()
    f_in = open(chosen_filename+'.in')
    f_out = open(chosen_filename+'.out', 'w')
    solve(f_in,f_out)
    f_in.close()
    f_out.close()


main_run()
