import re

i = open('A-large.in', 'r')
o = open('A-large.out', 'w')

T = int(i.readline())
casenum = 1
for j in range(T):
    input = re.split('\s+', i.readline())
    N = int(input[0])
    input = input[1:]
    commands = []
    for j in range(N):
        commands.append(input[2*j]+input[2*j+1])
    
    orange = []
    blue = []
    
    for command in commands:
        if re.match('O\d+', command):
            orange.append(command)
        else:
            blue.append(command)
    orangepos, bluepos = 1, 1
    time = 0
    while commands != []:
        buttonpress = False
        if blue != []:
            if bluepos == int(blue[0][1:]) and blue[0] == commands[0] and not buttonpress:
                buttonpress = True
                commands = commands[1:]
                blue = blue[1:]
            elif bluepos < int(blue[0][1:]):
                bluepos += 1
            elif bluepos > int(blue[0][1:]):
                bluepos -= 1
        if orange != []:
            if orangepos == int(orange[0][1:]) and orange[0] == commands[0] and not buttonpress:
                buttonpress = True
                commands = commands[1:]
                orange = orange[1:]
            elif orangepos < int(orange[0][1:]):
                orangepos += 1
            elif orangepos > int(orange[0][1:]):
                orangepos -= 1
        
        time += 1
            
    o.write('Case #'+str(casenum)+': '+str(time)+'\n')
    casenum += 1
    
i.close()
o.close()