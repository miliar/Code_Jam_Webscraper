kb = []
output = open('googlers.in', 'w')

def read(path):
    f = open(path)
    x = 1
    f.readline()
    for line in f:
        splits = line.split(" ")
        numberGooglers = int(splits[0])
        surprising = int(splits[1])
        best = int(splits[2])
        i = 3
        count = 0
        while i < len(splits) and numberGooglers > 0:
            if int(splits[i]) >= 3 * best:
                count = count + 1
            elif int(splits[i]):
                num = int(splits[i])
                if num + 2 >= best * 3:
                    count = count+1
                elif surprising > 0 and num + 4 >= best * 3:
                    count = count+1
                    surprising = surprising - 1
            i = i + 1
            numberGooglers = numberGooglers - 1
        toRet = str(count)
        output.write("Case #" + str(x) + ": " + toRet)
        output.write('\n')
        x = x + 1

def close():
    output.close()
