import sys

def numbers(input_s):   
    Transition = False
    s = [0] * len(input_s)
    ans = [0] * (len(input_s) + 1)
    for i in range(len(input_s)):
        s[i] = int(input_s[i])
    ans[len(input_s)] = 9
    for i in range(len(s) - 1, -1, -1):
        if (s[i] <= ans[i + 1]):
            ans[i] = s[i]
        else:
            ans[i] = s[i] - 1
            for j in range(i + 1, len(s)):
                ans[j] = 9
            
    result = 0
    if ans[0] == 0:
        for i in range(1, len(s)):
            result += ans[i] * 10**(len(ans) - i - 2)
    else:
        for i in range(len(s)):
            result += ans[i] * 10**(len(ans) - i - 2)
    return result
            
            
    
    
cin = open('B-small-attempt1.in', 'r')
cout = open('B-small-attempt1.out', 'w')
n = int(cin.readline())
for i in range(n):
    input_s = cin.readline().rstrip()
    ans = numbers(input_s)
    cout.write('Case #' + str(i + 1) + ': ' + str(ans) + '\n')
cin.close()
cout.close()
