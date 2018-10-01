import math

def read():
    return fin.readline().rstrip('\n')

def readIntList():
    return [int(x) for x in read().split(' ')]

def readFloatList():
    return [float(x) for x in read().split(' ')]    

def write(case, string):
    fout.write('Case #{0}: {1}\n'.format(case,string))

def main():

    mul = [[0, 1, 2, 3, 4, 5, 6, 7],
           [1, 4, 3, 6, 5, 0, 7, 2],
           [2, 7, 4, 1, 6, 3, 0, 5],
           [3, 2, 5, 4, 7, 6, 1, 0],
           [4, 5, 6, 7, 0, 1, 2, 3],
           [5, 0, 7, 2, 1, 4, 3, 6],
           [6, 3, 0, 5, 2, 7, 4, 1],
           [7, 6, 1, 0, 3, 2, 5, 4]]

    convert = { 'i' : 1,
                'j' : 2,
                'k' : 3}

    T = int(read())
    for tt in range(T):

        L, X = readIntList()
        string = read()

        letters = list()
        for i in string:
            letters.append(convert[i])

        state = 0
        val = 0
        possible = False

        for i in range(L*X):
            x = i % L
            y = letters[x]

            val = mul[val][y]

            if state == 0:
                if val == 1:
                    val = 0
                    state = 1
            elif state == 1:
                if val == 2:
                    val = 0
                    state = 2
            elif state == 2:
                if i == (L*X)-1 and val==3:
                    possible = True
                    break

        print(state, val)

        if possible:
            write(tt+1, "YES")
        else:
            write(tt+1, "NO")

    return 0

if __name__=="__main__":
    fin = open('input.txt','r')
    fout = open('output.txt', 'w')
    exit(main())