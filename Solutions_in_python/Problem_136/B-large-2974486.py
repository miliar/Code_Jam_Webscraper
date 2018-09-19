import sys
T = input()

def calc():
    C,F,X = [ float(value) for value in raw_input().split() ]
    current_cookies = 0.0
    current_production_rate = 2.0
    time = 0.0

    while True:
        win_with_factory = ((C-current_cookies)/current_production_rate)+X/(current_production_rate+F)
        win_without_factory = (X-current_cookies)/current_production_rate
        if win_with_factory > win_without_factory:
            return time+win_without_factory
        else:
            time += (C-current_cookies)/current_production_rate
            current_production_rate += F
            current_cookies = 0

for t in range(T):
    print("Case #%d: %.8f" % (t+1, calc()))


