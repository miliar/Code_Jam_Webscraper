# Google Code Jam Template

with open("c:\\Users\\Cole\\Downloads\\A-large.in","r") as input:
    in_file = input.readlines()
answers = []
T = in_file[0]
split = [line.split() for line in in_file[1:]]
cases = []
for line in split:
    N = int(line[0])
    case = [(line[i], int(line[i+1])) for i in range(1, 2*N+1, 2)]
    cases.append(case)
for case in cases:
    Oseq = [x for x in case if x[0] == 'O']
    Bseq = [x for x in case if x[0] == 'B']
    botseq = {'B':Bseq,'O':Oseq}
    time = 0
    pos = {'B' : 1,'O' : 1}
    while case != []:
        time += 1
        moved = {'B':False,'O':False}
        if pos[case[0][0]] == case[0][1]:
            moved[case[0][0]] = True
            del botseq[case[0][0]][0]
            del case[0]
        if moved['B'] == False and botseq['B'] != []:
            if pos['B'] < botseq['B'][0][1]:
                pos['B'] += 1
                moved['B'] = True
            elif pos['B'] > botseq['B'][0][1]:
                pos['B'] -= 1
                moved['B'] = True
            else:
                pass
        if moved['O'] == False and botseq['O'] != []:
            if pos['O'] < botseq['O'][0][1]:
                pos['O'] += 1
                moved['O'] = True
            elif pos['O'] > botseq['O'][0][1]:
                pos['O'] -= 1
                moved['O'] = True
            else:
                pass
    answers.append(str(time))
                                
with open("c:\\Users\\Cole\\Downloads\\A-large.out","w") as output:
    text = ""
    for x in range(len(answers)):
        text += ("Case #%d: %s\n" % (x+1, answers[x]))
    output.write(text)
