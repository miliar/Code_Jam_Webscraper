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
            
            
    
    
cin = open('A-large(1).in', 'r')
cout = open('A-large.out', 'w')
n = int(cin.readline())
for j in range(n):
    k, p = map(int, cin.readline().rstrip().split())
    s = list(map(int, cin.readline().rstrip().split()))
    ans = 0
    if (p == 2):
        p1 = 0
        for i in s:
            if i % 2 == 0:
                ans += 1
            else:
                p1 += 1         
        ans += (p1 + 1) // 2
    elif (p == 3):
        p1 = 0
        p2 = 0
        for i in s:
            if i % 3 == 0:
                ans += 1
            elif i % 3 == 1:
                p1 += 1
            else:
                p2 += 1
        m = min(p1, p2)
        ans += m
        p1 -= m
        p2 -= m
        ans += (p1 + p2 + 2) // 3
    else:
        p1 = 0
        p2 = 0
        p3 = 0
        for i in s:
            if i % 4 == 0:
                ans += 1
            elif i % 4 == 1:
                p1 += 1
            elif i % 4 == 2:
                p2 += 1
            else:
                p3 += 1
        m = min(p1, p3)
        ans += m
        p1 -= m
        p3 -= m
        ans += p2 // 2
        p2 = p2 % 2
        sum13 = p1 + p3
        if p2 == 1 and sum13 >= 2:
            ans += 1
            p2 = 0
            sum13 -= 2
        ans += sum13 // 4
        if (sum13 % 4 + p2 > 0):
            ans += 1
    cout.write('Case #' + str(j + 1) + ': ' + str(ans) + '\n')
cin.close()
cout.close()

