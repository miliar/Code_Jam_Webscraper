
import sys
sys.setrecursionlimit(1500)

def main():
    with open("pancake.txt") as f:
        content = f.readlines()
        
    c = [x.strip() for x in content] 

    T = int(c[0])

    for i, case in enumerate(c):
        if len(case.split()) < 2:
            continue
        pancake = case.split()[0]
        k = int(case.split()[1])
        times = len(pancake) - k + 1

        print "Case #" + str(i) + ":",
        if pancake.find("-") > -1:
            flip(k, pancake, times, 0)
        else:
            print "0"
        

def flip(k, pancake, times, f):
    times -= 1
    firstBlank = pancake.find("-")
    ps = list(pancake)
    if firstBlank > -1 and firstBlank + k < len(pancake) + 1:
        f += 1
        for i in range(firstBlank, firstBlank + k):
            if ps[i] == "+":
                ps[i] = "-"
            else :
                ps[i] = "+"

    result =  "".join(ps)

    nextBlank = result.find("-")
    if nextBlank > -1 and times > 0:
        flip(k, result, times, f)
    else:
        if nextBlank > -1:
            print "IMPOSSIBLE"
        else:
            print f

main()
