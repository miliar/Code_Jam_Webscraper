input = open("B-small-0.in")
output = open("B-small-0.out", "w")

T = int(input.readline())

for i in xrange(1, T + 1):
    case = input.readline().split(' ')
    comb = {}
    comb_list = case[1:int(case[0]) + 1]
    case[0:int(case[0]) + 1] = []
    opp = []
    opp_list = case[1:int(case[0]) + 1]
    case[0:int(case[0]) + 1] = []
    message = case[1]
    
    for c in comb_list:
        comb[c[0] + c[1]] = c[2]
        comb[c[1] + c[0]] = c[2]
        
    for o in opp_list:
        opp.append(o[0] + o[1])
        opp.append(o[1] + o[0])
    
    result = []
    for lt in xrange(len(message)):
        if len(result) == 0:
            result.append(message[lt])
        elif result[-1] + message[lt] in comb:
            result[-1] = comb[result[-1] + message[lt]]
        else:
            opposed = False
            for letter in result:
                if opp.count(letter + message[lt]):
                    opposed = True
                    break
            if opposed:
                result = []
            else:
                result.append(message[lt])
    
    if result[-1] == '\n':
        result[-1:] = []
    output.write("Case #" + str(i) + ": [")
    for l in result[:-1]:
        output.write(l + ", ")
    if len(result) > 0:
        output.write(result[-1] + "]\n")
    else:
        output.write("]\n")
    
input.close()
output.close()

