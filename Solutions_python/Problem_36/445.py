'''
Created on Sep 2, 2009

@author: Penn
'''
#
file=open("C-small-attempt3.in")
n=file.readline()
tests=[]
match="welcome to code jam"
check=[]
hashtables=[]
count=0
counts=[]


for i in range(0,int(n)):
    ah=file.readline()
    #print ah
    tests.append(ah.strip('\n').strip('\r'))

def construct(match, pos, input):
    global count
    for i in range(len(input)):
        if pos<len(match):
            if match[pos]==input[i]:
                #print match[pos], input[i]
                construct(match, pos+1, input[i+1:])
                if pos==len(match)-1:
                    count+=1

def trim(n):
    if n.find('w') > -1:
        n = n[n.find('w'):]
    else:
        return ''
    if n.rfind('m') > -1:
        n = n[0:n.rfind('m')+1]
    else:
        return ''
    return n

def run():
    global count
    for i in range(int(n)):
        count=0
        hashtables.append(construct(match, 0, trim(tests[i])))
        counts.append(count)

def format(n):
    answer=str(n)
    while len(answer) < 4:
        answer = '0' + answer
    while len(answer) > 4:
        answer = answer[1:]
    return answer

def result():
    for i, h in enumerate(hashtables):
        output.write("Case #%s: %s\n"%(i+1,format(counts[i])))

run()
output=open("output.out","w")
result()