#import numbers
import math


def checkNumber(n):
    s = math.sqrt(n)
    if not s.is_integer():
        return False
    s = str(int(s))
    tmp = str(n)
    if tmp == tmp[::-1] and s == s[::-1]:
        return True


def main():
    txtin = open("input.txt", "r")
    txtout = open("output.txt", "w")
    lines = txtin.readlines()
    cases = int(lines[0])
    writelines = []
    for i in range(1, cases+1):
        l = lines[i].split()
        a = int(l[0])
        b = int(l[1])
        count = 0
        for n in range(a, b+1):
            if checkNumber(n):
                count += 1
        res = "Case #" + str(i) + ": " + str(count) + '\n'
        writelines.append(res)
    txtout.writelines(writelines)

if __name__ == '__main__':
    main()
