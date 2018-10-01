# Google Code Jam Template

with open("c:\\Users\\Cole\\Downloads\\B-large.in","r") as input:
    in_file = input.readlines()
answers = []
N = in_file[0]
split = [x.split() for x in in_file[1:]]
cases = []
for x in split:
    combos = [x.pop(0) for n in range(int(x.pop(0)))]
    for i in range(len(combos)):
        if combos != []:
            bases = sorted(list(combos[i])[:2])
            result = list(combos[i])[2:]
            combos[i] = bases + result
    oppose = [x.pop(0) for n in range(int(x.pop(0)))]
    for i in range(len(oppose)):
        if oppose != []:
            a = list(oppose[i])
            a.sort()
            oppose[i] = a
    seq = list(x.pop(1))
    cases.append([combos, oppose, seq])

for case in cases:
    element_list = []
    for x in range(len(case[2])):
        element_list.append(case[2].pop(0))
        last = sorted(element_list[-2:])
        for combo in case[0]:
            if last == combo[:2]:
                del element_list[-2:]
                element_list.append(combo[2])
        for x in element_list:
            if element_list != []:
                if sorted([x, element_list[-1]]) in case[1]:
                    element_list = []
    answers.append(str(element_list).replace("'", ''))

with open("c:\\Users\\Cole\\Downloads\\B-large.out","w") as output:
    text = ""
    for x in range(len(answers)):
        text += ("Case #%d: %s\n" % (x+1, answers[x]))
    output.write(text)
