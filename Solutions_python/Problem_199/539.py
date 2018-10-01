fread = open('A-large.in')
lines = fread.readlines()
fw = open('output', 'w')

T = int(lines[0][0:-1])

for t in range(T):
    line = lines[t+1].split(" ")
    S = list(line[0])
    K = int(line[1])

    flips = 0
    for i in range(len(S)-K+1):
        if S[i]=='-':
            flips += 1
            for j in range(i, i+K):
                if S[j]=='+':
                    S[j] = '-'
                else:
                    S[j] = '+'

    allflipped = True
    for i in range(len(S)-K+1, len(S)):
        if S[i]=='-':
            allflipped = False

    result = ''
    if not allflipped:
        result = 'IMPOSSIBLE'
    else:
        result = str(flips)

    fw.write('Case #{}: {}\n'.format(t+1, result))
