import math
def cost(item, divisor):
    return math.ceil(item/divisor) - 1


def test(l):
    limit = max(l)
    for divisor in range(1,limit):
        total = divisor
        for i in l:
            total += cost(i, divisor)
        if total < limit:
            limit = total
    return limit

fin = open('input.in', 'r')
fout = open('output.txt' , 'w')

file = fin.read().split('\n')
file.pop(0)
a = file.pop(-1)
if a.isdecimal():
    file.append(a)

for count, line in enumerate(file):
    if count % 2 == 1:
        l = [int(x) for x in line.split()]
        out = test(l)
        fout.write("Case #{0}: {1}\n".format(count//2 + 1, out))
fout.close()
fin.close()
