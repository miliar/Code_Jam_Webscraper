import sys
sys.setrecursionlimit(10000)
def rec(c, f, x, num, smallest):
    new_small = compute(c, f, x, num)
    if new_small >= smallest: 
        return smallest
    else:
        return rec(c, f, x, num+1, new_small)

def compute(c, f, x, num):
    total = x / (2 + num * f)
    for i in range(num):
        total = total + c / (2 + i * f)
    return total

infile = open(sys.argv[1])
outfile = open("cookie_clicker_out", "w")

number = infile.readline().strip()
number = int(number)

for i in range(number):
    c, f, x = infile.readline().strip().split()
    c, f, x = float(c), float(f), float(x)

    smallest = rec(c, f, x, 1, x/2)

    outfile.write("Case #{0}: {1:.7f}\n".format(i+1, smallest))
