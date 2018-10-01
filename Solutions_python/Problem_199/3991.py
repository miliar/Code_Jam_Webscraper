inpFile = "A-small-attempt0.in"
outFile = "A-small-attempt0.out"

f = open('../../'+inpFile)
out = open('../../'+outFile, 'w')

T = int(f.readline())

def flip(arr, start, k):
    ret = list(arr)
    for i in range(start, start+k):
        c = arr[i]
        if c == '+':
            ret[i] = '-'
        else:
            ret[i] = '+'
    return ''.join(ret)

for t in range(1, T+1):
    line = f.readline().split(" ")
    pancake = original = line[0]
    k = int(line[1])
    count = 0
    while '-' in pancake:
        start = pancake.index('-')
        if start + k > len(pancake):
            count = "IMPOSSIBLE"
            break
        pancake = flip(pancake, start, k)
        if pancake == original:
            count = "IMPOSSIBLE"
            break
        else:
            count += 1
    out.write("Case #" + str(t) + ": " + str(count) + '\n')

f.close()
out.close()
