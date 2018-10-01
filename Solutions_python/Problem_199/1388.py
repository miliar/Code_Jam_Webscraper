from numpy import uint

def solve(s,k):
    mask = [1 for i in range(k)]
    target = makeTar(s)
    flips = []
    combine = ['0' for i in range(len(target))]
    for i,each in enumerate(target):
        if i>len(target)-k:
            break
        if int(int(each)^int(combine[i])):
            flips.append(i)
            for j,each in enumerate(mask):
                combine[i+j] = str(int(each)^int(combine[i+j]))
    return 'IMPOSSIBLE' if combine!=target else str(len(flips))

def makeTar(s):
    s = s.replace('+','0')
    s = s.replace('-','1')
    tar = list(s)
    return tar

file = open('problemABIG.txt', 'r')
array = []
for line in file:
    if line != '':
        array.append(line.replace('\n',''))
array = array[1:]
print(array)

with open('problemABIGsoln.txt','w',encoding='utf-8') as file:
    file.write('')
    for t,case in enumerate(array):
        file.write('Case #'+str(t+1)+': ' + solve(case.split(' ')[0],int(case.split(' ')[1])) + '\n')