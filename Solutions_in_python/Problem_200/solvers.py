

def find_lowerbound(number):

    # convert to list
    lijstje = [int(i) for i in str(number)]

    # find untidy
    untidy = 1
    i = 0
    size = len(lijstje)

    while i< (size-1) and lijstje[i] <= lijstje[i+1]:
        i = i + 1

    if i == size-1:
        return int(''.join(str(x) for x in lijstje))

    else:
    # fill zeros
        j = i + 1
        while j < size:
            lijstje[j] = 0
            j = j + 1
    return int(''.join(str(x) for x in lijstje)) - 1

