vowels = ['a','e','i','o','u']

def solve(text, n):
    """ find n-value of given text """
    result = []
    nc = 0 # nc is the last consonent after the current consonent in a longest stretch 
    for c in range (0, len(text)):
        if text[c] not in vowels:
            if nc <= c: 
                #start searching again 
                for t in range(c+1, len(text)):
                    if text[t]  in vowels:
                        nc = t - 1
                        break
                    elif t == len(text) - 1:
                        nc = t

            #calculate length of the stretch 
            if (nc - c + 1) >= n :
                u = c + n  - 1
                result.append((c, u))     
    #process result 
    m = set() 
    n_val = 0 
    for p in result:
        #get n-value of each pair
        #n_val += (p[0] + 1) * (len(text) - p[1])
        for s in range(0, p[0]+1):
            for e in range(p[1],len(text)) :
                t = (s,e)
                if t not in m:
                    n_val += 1
                    m.add(t)
            
    return n_val



if __name__== "__main__":
    with open("input_small") as f : 
        content = f.readlines()


    N = int(content[0])
    for case in range(0,N):
        (text, n) = content[case+1].split()
        print "Case #" + str(case + 1) + ": " + str(solve(text, int(n)))





