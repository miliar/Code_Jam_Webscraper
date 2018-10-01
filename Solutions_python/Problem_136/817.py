#!/usr/bin/python3




def time_for_cookies(C, F, X):
    from decimal import Decimal
    from decimal import setcontext
    from decimal import Context
    setcontext(Context(prec=10))
    time_taken = Decimal(0.0)

    current_cookies = Decimal(0.0)
    CPS = Decimal(2.0)
    wait_time = Decimal(0.0)
    buy_time = Decimal(0.0)

    if C > X > current_cookies:
        time_taken = X/CPS
        current_cookies = X
        return time_taken

    while current_cookies < X:


        if current_cookies >= C:
            wait_time = (X - current_cookies)/CPS
            buy_time = X/(CPS + F)
            
            if wait_time > buy_time:
                current_cookies = current_cookies - C
                CPS = CPS + F
                
            elif wait_time <= buy_time:
                time_taken = time_taken + (X - current_cookies) / CPS
                current_cookies = X

        elif current_cookies < C:
            wait_time = (C- current_cookies) / CPS
            current_cookies = C
            time_taken = time_taken + wait_time




    return time_taken


def give_nextline(filename):
    with open(filename) as in_file:
        for line in in_file:
            if line is not None:
                yield line
            else:
                yield None



def run_tests(filename):
    
    nextline = give_nextline(filename)
    TESTS = int(next(nextline))
    
    from decimal import Decimal
    from decimal import setcontext
    from decimal import Context
    setcontext(Context(prec=10))
    for it in range(1,TESTS + 1):
        C, F, X= map(Decimal, next(nextline).split(' ') )
        print('Case #' + str(it) + ': ' + str(time_for_cookies(C, F, X)))

    return
              

def main():
    import sys

    tests_file = sys.argv[1] if len(sys.argv) > 1 else "input.data"

    run_tests(tests_file)

main()
