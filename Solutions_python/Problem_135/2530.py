#! /usr/bin/python2.7
#-*-coding:utf-8-*


def magic(info1,mat1,info2,mat2):
    candidates = [c for c in mat1[info1-1]]

    candidates2 = []
    for c in mat2[info2-1]:
        if c in candidates:
            candidates2.append(c)

    if len(candidates2) ==1:
        return str(candidates2[0])
    elif len(candidates2) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"


def main():
    e = open("in", "r")
    s = open("out", "w")
    T = int(e.readline().split()[0])
    for t in xrange(0,T):
        info1 = int(e.readline().split()[0])

        mat1 = []
        for i in xrange(0,4):
            mat1.append([int(num) for num in e.readline().split()])


        info2 = int(e.readline().split()[0])
        mat2 = []
        for i in xrange(0,4):
            mat2.append([int(num) for num in e.readline().split()])

        s.write("Case #"+str(t+1)+": "+magic(info1,mat1,info2,mat2) + "\n")

    e.close()
    s.close()



if __name__ == '__main__':
    main()



