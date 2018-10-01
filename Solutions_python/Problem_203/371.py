
def solve(strs, R, C):
    for i in range(R):
        if strs[i] != ['?']*C:
            replace(strs[i])
            for j in range(len(strs[:i])):
                if strs[j] == ['?'] * C:
                    strs[j] = strs[i]
    char = []
    for i in range(R):
        if strs[i] != ['?']*C:
            char = strs[i]
        else:
            strs[i] = char
    return ["".join(strs[i]) for i in range(R)]
            
def replace(s):
    for i in range(len(s)):
        if s[i] != '?':
            for j in range(len(s[:i])):
                if s[j] == '?':
                    s[j] = s[i]
    char = ''
    for i in range(len(s)):
        if s[i] != '?':
            char = s[i]
        else:
            s[i] = char
    return s
        
            
        
a = 10
with open("in","r") as reader, open("out",'w') as writer:
    t = int(reader.readline())
    for i in range(t):
        R,C = map(int,reader.readline().split())
        strs = []
        for j in range(R):
            inp = list(reader.readline())
            if '\n' in inp:
                inp.remove('\n')
            strs.append(inp)
        writer.write("Case #" + str(i+1) + ":\n")
        res = solve(strs, R,C)
        for i in res:
            writer.write(i + "\n")
