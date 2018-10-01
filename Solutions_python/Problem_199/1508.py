# TODO: strip split


#f = open('A.in', 'r')
f = open('A-large.in', 'r')
g = open('outputfile.out', 'w')

T= int(f.readline())

myoutput = []

def processInput(pancakes, flipper):
    times = 0
    for i in range(len(pancakes)-flipper+1):
        if pancakes[i] =='-':
            times +=1
            #flip
            for j in range(flipper):
                if pancakes[i+j] =='+':
                    pancakes[i + j]  = '-'
                else:
                    pancakes[i + j]  = '+'

    for i in range (len(pancakes)-flipper+1, len(pancakes)):
        if pancakes[i]=='-':
            return 'IMPOSSIBLE'
    return times

for i in range(1,T+1):
    pancakes, flipper = f.readline().strip().split(' ')
    flipper = int(flipper)
    mypancakes={}
    for j in range(len(pancakes)):
        mypancakes[j] = pancakes[j]
    myoutput.append(processInput(mypancakes, flipper))


for i in range(1,T+1):
    g.write("Case #{}: {}\n".format(i, myoutput[i-1]))

f.close()
g.close()