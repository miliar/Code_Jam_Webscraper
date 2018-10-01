
with open('A-large.in') as f:
    content = f.readlines()
    
    
print(content[0])


f = open('output.txt', 'w')
testCase = 1

for line in content[1:]:
    numberOfSplits = 0
    split = line.split(" ")
    K = int(split[1])
    S = list(split[0])
    
    n = len(S)
    for i in range(0,n):
        if S[i] == '-':
            if i+K <= n:
                numberOfSplits = numberOfSplits + 1;
                for j in range(i,i+K):
                    if S[j] == '-':
                        S[j] = '+'
                    else:
                        S[j] = '-'
    
    impossible = False
    for c in S:
        if c == '-':
            impossible = True
            break
    
    print("-----")
    
    if impossible:
        f.write("Case #" + str(testCase) + ": IMPOSSIBLE\n")
    else:
        f.write("Case #" + str(testCase) + ": " + str(numberOfSplits) + "\n")
        
    testCase = testCase + 1
   
f.close()