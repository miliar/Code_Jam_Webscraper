f = open("A-large.in","r").readlines()
g = open("pancakes_large_output.txt",'w')
testcases = int(f[0])

for j in range(1,testcases+1):
    line = f[j].strip().split()
    pancakes = line[0]
    flipper = int(line[1])
    
    pancakes = list(pancakes)
    
    ans = 0
    for i in range(len(pancakes) - flipper + 1):
        if pancakes[i] == "-":
            ans += 1
            for m in range(i, i+flipper):
                if pancakes[m] == "+":
                    pancakes[m] = "-"
                else:
                    pancakes[m] = "+"    
    if "-" in pancakes:
        ans = "IMPOSSIBLE"
    
    g.write("Case #"+ str(j)+ ": "+ str(ans) +'\n')
