from sys import stdin as cin

cases=int(cin.readline())

def switch(string, start, size):
    for i in range(start, start+size):
        if string[i]=='-':
            string=string[:i]+'+'+string[i+1:]
        elif string[i]=='+':
            string=string[:i]+'-'+string[i+1:]
    return string

def are_all_up(pan):
    for i in pan:
        if i!='+':
            return False
    return True

for case in range(1, 1+cases):
    line=cin.readline().split()
    pancakes=line[0]
    size=int(line[1])
    flips=0
    for i in range(len(pancakes)):
        #print(i, pancakes)
        if pancakes[i]=='-':
            if i<=len(pancakes)-size:
                pancakes=switch(pancakes, i, size)
                flips+=1
            else:
                pancakes=switch(pancakes, len(pancakes)-size, size)
                flips+=1
    if are_all_up(pancakes):
        print("Case #"+str(case)+':', flips)
    else:
        print("Case #"+str(case)+':', 'IMPOSSIBLE')