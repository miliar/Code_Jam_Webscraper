small_in = "C-large.in"
small_out = "C-large.out"

infile = open(small_in)
T = int(infile.readline().rstrip())
output = ""
for i in range(T):
    N = int(infile.readline().rstrip())
    data = infile.readline().rstrip().split()
    numbers = []
    for n in data:
        numbers.append(int(n))
    numbers.sort()
    xor = numbers[0]
    max = 0
    for n in numbers[1:]:
        max = max + n
        xor = xor ^ n
    if xor == 0:
        result = str(max)
    else:
        result = "NO"
    output += "Case #" + str(i+1) + ": " + result + "\n"

outfile = open(small_out, 'w')
outfile.write(output)
