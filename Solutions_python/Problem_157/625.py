#!/usr/bin/python3
import re, sys, math

def main():
    with open(sys.argv[1]) as file:
        count = -2
        rc = 0
        case = 0
        repeat = 0
        for line in file.readlines():
            line = line.rstrip("\n")
            count += 1
            if count == -1:
                nbcases = int(line)
            else:
                if count % 2 == 0:
                    rc +=1
                    values = line.split(" ")
                    repeat = int(values[1])
                else:
                    motif = line
                    for i in range(0,repeat-1):
                        motif += line
                    print("Case #{}: {}".format(rc, treatMotif(motif)))

def treatMotif(motif):
    vi,si = findLetter("i", motif, 0)
    vj,sj = findLetter("j", motif, si)
    vk,sk = findLetter("k", motif, sj)
    v1 = treatRest(motif, sk)
    if vi and vj and vk and v1:
        return "YES"
    else:
        return "NO"

def treatRest(motif,start):
    if start < len(motif):
        curr = c2i(motif[start])
        for i in range(start+1, len(motif)):
            curr = ijkMult(curr, c2i(motif[i]))
        return curr == 1
    else:
        return True

def findLetter(letter, motif, start):
    val = False
    count = 1
    if len(motif) > 1 and start < len(motif):
        currenti = c2i(motif[start])
        while not currenti == c2i(letter) and start+count < len(motif):
            currenti = ijkMult(currenti, c2i(motif[start+count]))
            count += 1
        val = currenti == c2i(letter)
    return (val, start+count)
def c2i(a):
    if a == "i":
        return 2
    elif a == "j":
        return 3
    elif a == "k":
        return 4
    elif a == "a":
        return 1

def ijkMult(a,b):
    if (a < 0):
        return -ijkMult(-a,b)
    elif (b < 0):
        return -ijkMult(a,-b)
    elif (a == 1):
        return b
    elif (b == 1):
        return a
    elif (a == b):
        return -1
    elif (a == 2 and b == 3):
        return 4
    elif (a == 2 and b == 4):
        return -3
    elif (a == 3 and b == 4):
        return 2
    else:
        return -ijkMult(b,a)

if __name__ == "__main__":
    main()
