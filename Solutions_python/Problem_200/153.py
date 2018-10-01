def input(fname):
    lines = []
    with open(fname, 'r') as f:
        for line in f:
            lines.append(line)
    return lines


def output(fname, lines):
    with open(fname, 'w') as f:
        f.write('\n'.join(lines))

def solve(num):
    num = map(int, list(num[:-1]))
    i = 1
    j = -1
    while i < len(num) and num[i] >= num[i-1]:
        i+=1
    if i==len(num):
        return num
    j=i
    i-=1
    num[i]-=1
    i-=1
    while i>=0 and num[i]>num[i+1]:
        num[i+1] = 9
        num[i]-=1
        i-=1
    if not num[0]:
        return [9]*(len(num)-1)
    while j<len(num):
        num[j]=9
        j+=1
    return num


def main():
    lines = input('B-large.in')
    ans = []
    for c, num in enumerate(lines[1:]):
        s = ''.join(map(str, solve(num)))
        print "Case #{}: {}".format(c+1, ''.join(s))

if __name__ == "__main__":
    main()