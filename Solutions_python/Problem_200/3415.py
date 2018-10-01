import argparse

parser =  argparse.ArgumentParser(description='Google Code Jam 2017')
parser.add_argument('fin')
parser.add_argument('fout')

args = parser.parse_args()

fin = args.fin
fout = args.fout

def isTidy(s):
    l = []
    while s > 0:
        l.append(s % 10)
        s = s // 10
    l.reverse()
    print(l)
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def toList(s):
    l = []
    while s > 0:
        l.append(s % 10)
        s //= 10
    l.reverse()
    return l

def solver(s):
    current = s
    while(True):
        #print(current)
        l = toList(current)
        for i in range(len(l)):
            if i == len(l) - 1:
                return current
            if l[i] > l[i+1]:
                current -= (l[i+1]+1) * 10 ** (len(l)-i-2)
                temp = toList(current)
                for j in range(i+1, len(temp)):
                    #print(i,j,len(temp),temp)
                    temp[j] = 9
                current = int("".join([str(c) for c in temp]))
                break

with open(fin,'r') as input, open(fout,'w') as output:
    T = int(input.readline().rstrip('\n'))
    for i in range(0,T):
        s = input.readline().rstrip('\n')
        s = int(s)
        answer = 'Case #{}: {}\n'.format(i+1,solver(s))
        print(answer)
        output.write(answer)