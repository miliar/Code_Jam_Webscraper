def main():
    f = open("./A-large.in")
    g = open("./output","w")
    
    numcases = int(f.readline())
    for casenumber in range(numcases):
        s = f.readline()
        s = s[:-1]
        l = list(s)
        se = set(l)
        base = len(se)
        
        assigned = {}
        for x in se:
            assigned[x] = -1
            
        
        assigned[s[0]] = 1
        i = 0
        while(i<=len(s)-1 and s[i]==s[0]):
            i = i+1
        if(i!= len(s)):
            assigned[s[i]]= 0
        else:
            base = 2
        
        count = 2
        for i in range(len(s)):
            if assigned[s[i]]==-1:
                assigned[s[i]] = count
                count = count + 1
        
        l.reverse()
        ans = assigned[s[0]]
        tmp = s[1:]
        for x in tmp:
            ans = ans*base +assigned[x]

        print base
        print assigned
        
        s = "Case #" + str(casenumber+1) + ": " + str(ans) + "\n" 
        g.write(s)
