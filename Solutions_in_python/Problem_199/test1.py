def solve(input, flipper_size):
    changes = 0
    count = 0
    flip = False
    for i in range(0, (len(input)+1)-flipper_size):
        if(input[i]=='+'):
            continue;
        for j in range(i,i+flipper_size):
            if(input[j]=='-'):
                flip = True
        if(flip == True):
            changes += 1
            for k in range(i,i+flipper_size):
                if(input[k]=='-'):
                    input[k] = '+'
                elif(input[k]=='+'):
                    input[k] = '-'
            flip = False
    for i in range(0, len(input)):
        if input[i] == '+':
            count += 1
    #print("final input: ", input)
    #print("count: ", count)
    if count == len(input):
        return changes
    else:
        return "IMPOSSIBLE"

if __name__ == "__main__":
    f = open("C://input.in","r")
    linelist = f.readlines()
    no_of_input = len(linelist)
    input = list()
    flipper_size = 0
    final_output = ''
    for case in range(1, no_of_input):
        del input[:]
        S = linelist[case].strip()

        last_val = ['0','1','2','3','4','5','6','7','8','9']
        if any(ext in S[-2] for ext in last_val):
            val=S[-2]+S[-1]
            flipper_size = int(val)
            S = S[:-2]
            S = S[:-1]
            S = S.strip()
        else:
            flipper_size = int(S[-1])
            S = S[:-1]
            S = S.strip()

        for i in range(0, len(S)):
            input.append(S[i])
        solution = solve(input, flipper_size)
        final_output = final_output+("Case #{0}: {1}\n".format(case, solution))
    f.close()
    fw = open('myfile1.out', 'w')
    fw.write(final_output)  # python will convert \n to os.linesep
    fw.close()  # you can omit in most cases as the destructor will call it
