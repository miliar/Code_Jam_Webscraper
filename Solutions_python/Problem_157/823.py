import codecs
with codecs.open('2.txt', 'r', 'utf-8') as f:
    a = f.readlines()
output = ''
counter = 0
def fun(a, b):
    res = a[1]*b[1]
    if a[0] == 1:
        return [b[0], res]
    if b[0] == 1:
        return [a[0], res]
    if a[0] == 'i':
        if b[0] == 'i':
            return [1, res*-1]
        if b[0] == 'j':
            return ['k', res]
        if b[0] == 'k':
            return ['j', res*-1]
    if a[0] == 'j':
        if b[0] == 'i':
            return ['k', res*-1]
        if b[0] == 'j':
            return [1, res*-1]
        if b[0] == 'k':
            return ['i', res]
    if a[0] == 'k':
        if b[0] == 'i':
            return ['j', res]
        if b[0] == 'j':
            return ['i', res*-1]
        if b[0] == 'k':
            return [1, res*-1]
def a_next(a):
    if a[0] == 'i':
        return ['j', 1]
    if a[0] == 'j':
        return ['k', 1]
    if a[0] == 'k':
        return ['l', 1]
#
for i in range(len(a[1:])/2):
    counter += 1
    line = a[(2*i)+1]
    nextline = a[(2*i)+2].strip()
    x = int(line.split(' ')[1].strip())
    string = x*nextline
    curser = [1, 1]
    num = len(string)
    needed = ['i', 1]
    done = False
    for j in range(num):
        curser = fun(curser, [string[j], 1])
        if curser == needed:
            if curser == ['k', 1]:
                done = True
            needed = a_next(curser)
            curser = [1, 1]
    if done and curser == [1, 1]:
        output += 'Case #%d: %s\n' % (counter, 'YES')
    else:
        output += 'Case #%d: %s\n' % (counter, 'NO')
with codecs.open('2_o.txt', 'w', 'utf-8') as f:
    f.write(output)
