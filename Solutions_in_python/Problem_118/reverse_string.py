def reverse(s):
    new = ""
    t = len(s)
    for i in range(t):
        new += s[t-i-1]

    return new
        
        
