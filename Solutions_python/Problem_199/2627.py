#!/usr/bin/python
import pdb
case = 'A'

def func(i, datum):
    string = list(datum.split(' ')[0])
    K = int(datum.split(' ')[1])
    c = 0
#    pdb.set_trace()
    for j in range(0, len(string)-K+1):
        if string[j]=='-':
            c=c+1
            for k in range(j, j+K):
                if string[k]=='-':
                    string[k]='+'
                else:
                    string[k]='-'
    success = True
    for j in range(0, len(string)):
        if string[j] == '-':
            return "IMPOSSIBLE"
    if success:
        return c


def get(file_handler, row_per_case=1):
    result = []
    if row_per_case==1:
        return file_handler.readline()
    for i in range(0, row_per_case):
        result.append(file_handler.readline())
    return result


f = open('/tmp/'+case+'.in', 'r')
n = int(f.readline())
file_output = open('/tmp/'+case+'.out', 'w')
for i in range(0,n):
    datum = get(file_handler=f)
    result = func(i, datum)
    output = 'Case #'+str(i+1)+": "+str(result)
    print output
    file_output.write(output+'\n')

