import math

def pos_max(n,k):
    if (k != 1):
        exp = math.floor(math.log2(k))
        num = math.pow(2,exp) + n - k
        denom = math.pow(2, exp + 1)
        return(num // denom)
    else:
        return(n//2)

def pos_min(n,k):
    exp = math.floor(math.log2(k))
    num = n - math.pow(2,exp)
    return(pos_max(num,k))

infile = open("C-small-2-attempt0.in",'r')
out = open("out.txt", 'w')
num_prob = int(infile.readline())
i = 0
for line in infile:
    i += 1
    n, k = [int(s) for s in line.split(" ")]
    val = "Case #{}: {} {}\n".format(i, int(pos_max(n,k)), int(pos_min(n,k)))
    out.write(val)
infile.close()
out.close()