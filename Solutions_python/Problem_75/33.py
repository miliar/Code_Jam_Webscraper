#!/usr/bin/env python


def combine(crule,orule,string,input):
    if string =='':
        return input
    pattern = ''.join(sorted(string[-1]+input))
    if pattern in crule.keys():
        return step(crule,orule,string[:-1],crule[pattern])
    return string + input

def reduce(orule,string):
    for ch in string[:-1]:
        pattern = ''.join(sorted(ch+string[-1])) 
        if pattern in orule:
            return ''
    return string 
 
def step(crule,orule,string,input):
    oldstring = string
    string = combine(crule,orule,string,input)
    if oldstring+input == string:
        string = reduce(orule,string)
        return string 
    else:
        return string

def cparse(crule,string):
    crule[str(''.join(sorted(string[0:2])))] = string[-1]

def oparse(orule,string):
    orule.append(''.join(sorted(string)))

if __name__ == '__main__':
    f = open('input')
    a = int( f.readline() )
    for cn in range(a):
        line = f.readline().split()
        crule = {}
        orule = []
        cursor = 0
        cnumber = int(line[cursor])
        for i in range(cursor+1,cursor+1+cnumber):
            cparse(crule,line[i])
        cursor += (1+cnumber)
        onumber = int(line[cursor])
        for i in range(cursor+1,cursor+1+onumber):
            oparse(orule,line[i])
        cursor += (1+onumber)
        length = int(line[cursor])
        string = line[-1]
        rs = string[0]
        for j in range(1,length):
            rs = step(crule,orule,rs,string[j])
        print "Case #"+str(cn+1)+":", ''.join(str(list(rs)).split("'"))
