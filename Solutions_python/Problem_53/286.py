import math

def int_input():
    return int(raw_input())

def list_int_input():
    return map(int, raw_input().split())

def main():
    for c in range(int_input()):
        n, k = list_int_input()
        loop_len = math.pow(2, n)
        if k % loop_len == loop_len - 1:
            print 'Case #%d: ON' % (c+1)
        else:
            print 'Case #%d: OFF' % (c+1)

main()
