name = 'A'
typ = 'large'
base = name+'-'+typ+'.'
lines = file(base+'in').readlines()

lines = [line.replace('\n','') for line in lines]

def parse(tree):
    ch = 1
    while not (tree[ch].isdigit() or tree[ch] == '.'): ch += 1
    mul_start = ch
    while tree[ch] != ' ' and tree[ch] != ')': ch += 1
    mul_end = ch
    mul = float(tree[mul_start:mul_end])
    while tree[ch] == ' ' or tree[ch] == ')':
        if tree[ch] == ')':return ((mul,),tree[ch:])
        ch += 1
    prop_start = ch
    while tree[ch] != ' ' and tree[ch] != ')': ch += 1
    prop_end = ch
    prop = tree[prop_start:prop_end]
    while tree[ch] != '(': ch += 1
    first_sub,left = parse(tree[ch:])
    second_sub,left = parse(left)
    ch = 0
    while left[ch] != ')': ch += 1
    return ((mul,prop,first_sub,second_sub),left[ch+1:])

def find_val(tree,props):
    score = tree[0]
    if len(tree)>1:
        if tree[1] in props:
            score *= find_val(tree[2],props)
        else:
            score *= find_val(tree[3],props)
    return score

N = int(lines[0])
fpos = 1
out = file(base+'out','wb')
for case in xrange(1,N+1):
    L = int(lines[fpos])
    fpos += 1
    tree = " ".join(lines[fpos:fpos+L])
    fpos += L
    A = int(lines[fpos])
    fpos += 1
    animals = lines[fpos:fpos+A]
    fpos += A
    for i in xrange(len(animals)):
        temp = animals[i]
        temp = temp.split(' ')
        temp = [temp[0]]+[set([temp[j+2] for j in xrange(int(temp[1]))])]
        animals[i] = temp
    
    tree = parse(tree)[0]
    out.write('Case #%d:\n' % case)
    for animal in animals:
        out.write(('%.7f' % find_val(tree,animal[1])) + '\n')

out.close()
