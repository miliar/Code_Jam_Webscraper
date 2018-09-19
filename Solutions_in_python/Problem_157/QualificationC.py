def mult(one, two):
    negs = 0
    ret = ''

    if list(one)[0] == '-':
        negs += 1
        one = list(one)[1]
    if list(two)[0] == '-':
        negs += 1
        two = list(two)[1]

    if one == '1':
        ret = two
    if two == '1':
        ret = one

    if one == 'i':
        if two == 'i':
            ret = '-1'
        if two == 'j':
            ret = 'k'
        if two == 'k':
            ret = '-j'

    if one == 'j':
        if two == 'i':
            ret = '-k'
        if two == 'j':
            ret = '-1'
        if two == 'k':
            ret = 'i'

    if one == 'k':
        if two == 'i':
            ret = 'j'
        if two == 'j':
            ret = '-i'
        if two == 'k':
            ret = '-1'

    if len(list(ret))<1:
        print([one, two])

    if negs == 1:
        if list(ret)[0] == '-':
            return list(ret)[1]
        else:
            return '-'+ret
    else:
        return ret


def reduce(ijk):
    lst = list(ijk)
    holder = lst[0]

    for x in range(1, len(lst)):
        holder = mult(holder, lst[x])

    return holder


def search(ch, ijk):

    if ch == ['k']:
        return reduce(ijk) == 'k'

    if len(ijk) < len(ch):
        return False

    if reduce(ijk) != reduce(''.join(ch)):
        return False

    for x in range(0, len(ijk)):
        if reduce(ijk[:(x+1)]) == ch[0]:
            if search(ch[1:], ijk[(x+1):]):
                return True
    return False


with open('C-small-attempt1.in') as f:
    stuff = f.readlines()

x = 1
case = 1

while x < (len(stuff)):

    part = (stuff[x+1].replace("\n", ''))

    if (part.count('i') == len(part)) | (part.count('j') == len(part)) | (part.count('k') == len(part)):
        print("Case #"+str(case)+": NO")

    else:
        trial = int(stuff[x].split()[1])*(stuff[x+1].replace("\n", ''))
        if search(['i', 'j', 'k'], trial):
            print("Case #"+str(case)+": YES")
        else:
            print("Case #"+str(case)+": NO")

    x += 2
    case += 1
