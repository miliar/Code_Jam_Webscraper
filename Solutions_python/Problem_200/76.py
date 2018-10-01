def f(s):
    lastVal = int(s[0])
    lastPos = 0

    for i in range(1, len(s)):
        val = int(s[i])
        if val < lastVal:
            return int(s[:lastPos] + str(lastVal-1) + '9'*(len(s)-lastPos-1))
            
        elif val > lastVal:
            lastVal = val
            lastPos = i
    
    return int(s)

t = int(input())
for i in range(t):
    print('Case #' + str(i+1) + ':', f(input()))
    
