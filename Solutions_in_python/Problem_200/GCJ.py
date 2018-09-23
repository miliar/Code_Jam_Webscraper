
inputfile = "B-small-attempt0.in"
outputfile = "output.txt"
o = open(outputfile, "w")



def cal(num):
    for n in range(num, 0 ,-1):
        lst = [int(i) for i in str(n)]
        y = lst
        if y == sorted(lst):
            o.write(str(n))
            o.write('\n')
            break



m=0
with open(inputfile,"r") as i: #helps better with erors
    n = i.readline()
    for l in range(int(n)):
        m+=1
        num = int(i.readline())
        s = "Case #" + str(m) +": "
        o.write(s)
        cal(num)

o.close()
