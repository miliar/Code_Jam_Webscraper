import sys

def generator(N):
    string = '1'

    for x in range(N):
        string = string + '0'

    string = string + '1'

    return string

def switcher(string, index):
    x = 0
    return_string = ''
    for element in string:
        if x == index:
            return_string = return_string + '1'

        else:
            return_string = return_string + element
        x += 1
    return return_string


def best_option(string):
    flist = []
    for x in range(len(string)):


        if string[x] == '0':

            ls, rs = 0, 0
            swap = string[:x]

            for l in swap[::-1]:

                if l == '0':
                    ls += 1
                else:
                    break


            for r in string[x + 1:]:
                if r == '0':
                    rs += 1

                else:
                    break

            flist.append([ls, rs, x])
    past_minimum = 0
    cordX, cordLS, cordRS = 0, 0, 0,

    for element in flist:
        minimum = min(element[0], element[1])
        ls, rs, x = int(element[0]), int(element[1]), int(element[2])


        if minimum > past_minimum:
            past_minimum = minimum
            index = x
            cordLS, cordRS, cordX = ls, rs, x

        if minimum == past_minimum:

            if max(ls, rs) > max (cordLS, cordRS):
                cordLS, cordRS, cordX = ls, rs, x
                index = x


            elif max(ls, rs) == max(cordLS, cordRS):
                if rs <= ls:
                    index = x
                    cordX = index
                    cordLS = ls
                    cordRS = rs
                else:
                    index = cordX
        if index == 0:
            index = cordX

    return (cordLS, cordRS, index)

def checker(string):
    for element in string:
        if element == '0':
            return True
            break

    return False


def solver(N,K):
    string = generator(N)
    n = 0
    while n != K:
        LS, RS, index = best_option(string)
        string = switcher(string, index)

        n += 1
        if checker(string) != True:
            break
    return (max(LS, RS), min(LS, RS))



def inputer(input):
    with open (input) as fin:
        finx = fin.read().split('\n')
        biglist = []
        biglist = [line.strip().split(' ') for line in finx]
        biglist = biglist[1:-1]
        return (biglist)

biglist = inputer(sys.argv[1] + '.in')
return_list = []
for element in biglist:
    N, K = int(element[0]), int(element[1])
    maxima, minima = solver(N, K)
    return_list.append('%d %d' % (maxima, minima))
    print (x)

def outputer(output, return_list):
    with open(output, 'w') as out:
        x = 1
        for element in return_list:
            out.write('Case #%d: %s \n' % (x, element))
            x += 1

outputer(sys.argv[1] + '.out', return_list)
