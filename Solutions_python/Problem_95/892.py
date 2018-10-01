from string import rstrip
from sys import stdin, stdout

input = []
for line in stdin: input.append(rstrip(line,'\n'))
nTestCases = int(input.pop(0))
testcase = 1

map = {
    'o':'e',
    'q':'z',
}

first = "our language is impossible to understand".replace(' ','')
second = "there are twenty six factorial possibilities".replace(' ','')
third = "so it is okay if you want to just give up".replace(' ','')
fe = "ejp mysljylc kd kxveddknmc re jsicpdrysi".replace(' ','')
se = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd".replace(' ','')
te = "de kr kd eoya kw aej tysr re ujdr lkgc jv".replace(' ','')

for i in range(len(fe)): map[fe[i]]=first[i]
for i in range(len(se)): map[se[i]]=second[i]
for i in range(len(te)): map[te[i]]=third[i]

while True:
    stdout.write("Case #%s: "%testcase)
    tokens = input[testcase-1].split(' ')
    for token in tokens:
        td = ''
        for c in token:
            if c in map:
                td+=map[c]
            else:
                td+='q'
        stdout.write(td)
        stdout.write(" ")
    stdout.write("\n")
    if testcase >= nTestCases: break
    testcase +=1

