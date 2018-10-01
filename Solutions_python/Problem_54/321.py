def even(x):
    return (x % 2 == 0)

def gcd(x, y):
    if (x < y):
        return gcd(y, x)
    if (y == 0):
        return x
    else:
        if even(x):
            if even(y):
                return (gcd(x >> 1, y >> 1) << 1)
            else:
                return gcd(x >> 1, y)
        else:
            if even(y):
                return gcd(x, y >> 1)
            else:
                return gcd(y, x - y)
            
f = open("B-large.in")
case = int(f.readline())
string = ''
for k in range(case):
    line = f.readline().rstrip("\n")
    item = line.split()
    count = int(item[0])
    item = item[1:]
    for i in range(count):
        item[i] = int(item[i])    
    item.sort()
    item.reverse()
    num = None
    for i in range(count-1):
        if num == None:
            num = item[i] - item[i+1]
        else:
            num = gcd(num, item[i] - item[i+1])
    year = item[-1] % num
    if year == 0:
        string += "Case #" + str(k+1) + ": " + str(year) + "\n"
    else:
        string += "Case #" + str(k+1) + ": " + str(num - year) + "\n"
    
o = open('B-large-o.in', 'w')
o.write(string)
o.close()

