import sys

def magicka(combos, cancels, invokes):
    elist = []
    for invoke in invokes:
        elist += [invoke]
        if len(elist) > 1:
            for combo in combos:
                if invoke == combo[0][0] and elist[-2] == combo[0][1]:
                    elist[-2:] = [combo[1]]
                elif invoke == combo[0][1] and elist[-2] == combo[0][0]:
                    elist[-2:] = [combo[1]]
            for cancel in cancels:
                if cancel[0] in elist and cancel[1] in elist: elist = []
    return str(elist).replace("'", '')

def main(filename):
    Input = open(filename, 'r').read().split('\n')
    Output = ""
    for i in range(int(Input[0])):
        line = Input[i + 1].split(' ')
        combos = line[1:int(line[0]) + 1]
        combos = [[combo[:2], combo[2:]] for combo in combos]
        line = line[int(line[0]) + 1:]
        cancels = line[1:int(line[0]) + 1]
        invokes = line[-1]
        result = magicka(combos, cancels, invokes)
        Output += "Case #" + str(i + 1) + ": " + result + "\n"
    open(filename[:-3] + ".out", 'w').write(Output)

if __name__ == "__main__":
    main(sys.argv[1])
