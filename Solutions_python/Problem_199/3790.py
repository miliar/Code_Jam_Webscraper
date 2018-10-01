# coding: utf-8

def flip(tmpCakeStr, k):
    sb = list(tmpCakeStr)
    for i in range(k):
        sb[i] = '-' if tmpCakeStr[i] == '+' else '+'
    return ''.join(sb)


def removeFirstUpCakes(cakeStr):
    pointer = 0
    cakeStrLen = len(cakeStr)
    while pointer < cakeStrLen and cakeStr[pointer] == '+':
        pointer += 1
    return cakeStr[pointer:]
with open('/Users/vh-mac/Downloads/A-large.in', 'r') as infile:
    T = int(infile.readline())
    counter = 0
    results = []
    while(T > counter):
        counter += 1
        inputs = infile.readline().split()
        S = inputs[0]
        K = int(inputs[1])
        count = 0
        tmpCakeStr = S
        while (len(tmpCakeStr) > 0 and len(tmpCakeStr) >= K):
            tmpCakeStr = removeFirstUpCakes(tmpCakeStr)
            if (len(tmpCakeStr) >= K):
                count += 1
                tmpCakeStr = flip(tmpCakeStr, K)
        result = str(count) if len(tmpCakeStr) == 0 else "IMPOSSIBLE"
        results.append("Case #{}: {}".format(counter, result))
        print("Case #{}: {}".format(counter, result))
    infile.close()
with open('As.out', 'w') as outfile:
    outfile.write('\n'.join(results))
    outfile.close()