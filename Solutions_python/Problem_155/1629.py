'''
Created on 10 apr. 2015

@author: Kristian
'''


lines = [line.strip() for line in open('inL.txt')]
out = open('./out.txt', 'w+')

for case in range(1, len(lines)):
    line = lines[case]
    spl = line.split()
    audience = map(int, list(spl[1]))
    clapping = 0
    friends_needed = 0
    
    for i in range(len(audience)):
        clapping += audience[i]
        if clapping < (i+1):
            friends_needed += 1
            clapping += 1
    out.write("Case #" + str(case) + ": " + str(friends_needed) + "\n")
out.close()