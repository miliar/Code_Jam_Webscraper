#!/usr/bin/python3

def tidy_number(last_counted):        
    for n in range(last_counted, 0, -1):        
        numbers = list(map(ord,str(n)))
        if numbers == sorted(numbers):
            return int(''.join(map(chr,numbers)))

test_ct = int(input())
i = 1
while True:
    try:        
        param = int(input().strip())
        print("Case #{}: {}".format(i, tidy_number(param)))
        i += 1
    except Exception:
        break
