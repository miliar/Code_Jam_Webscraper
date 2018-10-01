

file = open("A-large.in","r")
ldn = []
for i in file.readline().split(" "):
    ldn.append(int(i))
L = ldn[0]
D = ldn[1]
N = ldn[2]

words = []
for i in range(D):
    words.append(file.readline().strip())

testcases = []
for i in range(N):
    testcases.append(file.readline().strip())

def main():
    i = 0
    for case in testcases:
        value = 0
        for word in words:
            value += checkCaseWithWord(case,word)
        print "Case #"+str(i+1)+": "+str(value)
        i+=1

def checkCaseWithWord(case,word):
    values = []
    start = 0
    keep = True
    pos=0
    outside = True
    for i in range(len(case)):
        if keep:
            if case[i] == "(":
                start = i
                outside = False
            else:
                if case[i] == ")":
                    if not checkGroupAgainstLetter(case[start+1:i],word[pos]):
                        keep = False
                    pos = pos + 1
                    outside = True
                else:
                    if outside and case[i] >= "a" and case[i] <= "z":
                        if case[i] != word[pos]:
                            keep = False
                        pos = pos + 1

    return keep
                            

def checkGroupAgainstLetter(group,letter):
    for i in group:
        if i == letter:
            return 1
    return 0
    
main()
