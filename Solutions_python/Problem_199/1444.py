#!/usr/bin/python
def Oversize_pancake():
    T = int(raw_input())
    for i in xrange(1,T+1):
        S, K = raw_input().split()
        #print S, K
        k = int(K)
        s = list(S)
        #print S,k
        ct = flipct(s,k)
        print "Case #"+ str(i)+ ":",
        if ct == float("-inf"):
            print "IMPOSSIBLE"
        else: print ct

def flipct(s,k):
    if '-' not in s: return 0
    n = len(s)
    ct = 0
    for i in range(n-k+1):
        if s[i] == '-':
            for j in range(i,i+k):
                if s[j] == '+':
                    s[j] = '-'
                else: s[j] = '+'
            #print s
            ct += 1
    
    if '-' in s:
        return float("-inf")
    else:
        return ct

# def flip(s,k):
#     print s, 235
#     for i in range(len(s)):
#         if s[i] == '+':
#             s[i] = '-'
#         else:
#             s[i] = '+'
#     print s, 235 


# def flipct(s,k):
#     if '-' not in s: return 0
#     n = len(s)
#     if n == 0: return 0
#     if n < k: return float("-inf")
#     if s[0] == '+': return flipct(s[1:],k)
#     for i in range(k,0,-1):
#         if s[0:k] == '-'*k and i ==k: 
#             return 1 + flipct(s[k:],k)
#         elif i < k and s[0:k] == ('-'*i + '+'*(k-i)):
#             if k+i-1 < n and s[k:k+i] == '-'*i:
#                 return 2 + flipct(s[k+i:],k)
#             else: return float("-inf")
#     return float("-inf")
        



if __name__ == "__main__":
    Oversize_pancake()




