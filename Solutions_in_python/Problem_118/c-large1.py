from math import sqrt, ceil

# bases = []

def is_palindrome(num):
    return str(num) == "".join(reversed(str(num)))

# def build_bases(a,b):
#     for i in range(a,b+1):
#         if is_palindrome(i) and is_palindrome(i**2):
#             bases.append(i)

bases = [1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002,
         10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001,
         101101, 110011, 111111, 200002, 1000001, 1001001, 1002001,
         1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111,
         1111111, 2000002, 2001002]

def solve(A,B):
    a = int(ceil(sqrt(A)))
    b = int(sqrt(B))
    start = 0
    while start < len(bases) and bases[start] < a:
        start +=1
    end = start
    while end < len(bases) and bases[end] <= b:
        end += 1
    return end-start
        

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        A,B = [int(x) for x in raw_input().split()]
        print "Case #%d: %d" % (i, solve(A,B))
