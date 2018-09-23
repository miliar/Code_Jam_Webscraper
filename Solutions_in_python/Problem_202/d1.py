from multiprocessing import Pool
import sys
from subprocess import run

# cut input
script, fin = sys.argv
fin = open(fin)
fout1 = open("in1.in","w")
fout2 = open("in2.in","w")
fout3 = open("in3.in","w")

strgroup = set(['+','x','o'])

i = 0
for line in fin:
    # print(i)
    if i is 0:
        n = int(line)
        # print(n)
        i += 1
        continue
    # print(line)
    if line[0] not in strgroup:
        i += 1
    fout = fout1
    if i < 32:
        fout = fout1
    elif i < 62:
        fout = fout2
    else:
        fout = fout3
    fout.write(line)

fout1.close()
fout2.close()
fout3.close()


def run1(s):
    from subprocess import run
    if s == 1:
        run(["python", "d2.py", "1", "30"], stdin=open("in1.in"), stdout=open("out1.out", "w"))
    elif s == 2:
        run(["python", "d2.py", "31", "60"], stdin=open("in2.in"), stdout=open("out2.out", "w"))
    else:
        run(["python", "d2.py", "61", str(n)], stdin=open("in3.in"), stdout=open("out3.out", "w"))



p = Pool(4)
p.map(run1, [1,2,3])

"""
p.apply_async(run(["python", "d2.py", "1", "30"], stdin=open("in1.in"), stdout=open("out1.out", "w")))
p.apply_async(run(["python", "d2.py", "31", "60"], stdin=open("in2.in"), stdout=open("out2.out", "w")))
p.apply_async(run(["python", "d2.py", "61", str(n)], stdin=open("in3.in"), stdout=open("out3.out", "w")))
p.close()
p.join()
"""
run(["cat", "out1.out", "out2.out", "out3.out"], stdout=open("fout.out", "w"))
