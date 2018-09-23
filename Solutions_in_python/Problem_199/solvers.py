

def pancakesLeftToRight(s: list, K: int):
    i = 0
    escape = 0
    escapeLevel = 1000001
    nrOfFlips = 0
    output = 'IMPOSSIBLE'
    length = len(s)
    while i <= ( length - K ) and escape < escapeLevel:
        if s[i] == '+':
            i = i + 1
        else:
            flip(s, i, K)
            nrOfFlips = nrOfFlips + 1

        escape = escape + 1


    #check impossible
    if '-' not in s:
        output = nrOfFlips

    if escape >= escapeLevel:
        output = 'Escapelevel gehaald, check de input en code'

    return output


def flip(string: list, start: int, length: int):
    for i in range(start, start+length):
        flip_one(string=string, location=i)
    return string


def flip_one(string: list, location: int):
    if string[location] == '+':
        string[location] = '-'
    elif string[location] == '-':
        string[location] = '+'
    else:
        print('Error, tried to flip ', str(string[location]))
    return string