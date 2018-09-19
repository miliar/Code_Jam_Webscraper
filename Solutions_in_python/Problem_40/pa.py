def readInts():
    s = raw_input()
    return [int(ss) for ss in s.split()]

def next_token(str, i):
    buf = ''
    for i in range(i, len(str)):
        if str[i] == '(':
            if buf:
                return (buf, i)
            else:
                return ('(', i + 1)
        elif str[i] == ')':
            if buf:
                return (buf, i)
            else:
                return (')', i + 1)
        elif str[i] == ' ':
            if buf:
                return (buf, i + 1)
            else:
                continue
        else:
            buf += str[i]
    return (buf, len(str))

def feature(str, pos):
    node = {}
    
    # furry
    name, pos = next_token(str, pos)
    if name == ')':
        return None, None
    node['name'] = name
    
    # (
    ignore, pos = next_token(str, pos)
    
    # 0.81
    lposibility, pos = next_token(str, pos)
    node['lp'] = lposibility
    
    # ) or name
    tmp, newpos = next_token(str, pos)
    if tmp == ')':
        pos = newpos
    else:
        lchild, newpos = feature(str, pos)
        # )
        ignore, pos = next_token(str, newpos)
        node['lc'] = lchild
        
    # (
    ignore, pos = next_token(str, pos)

    # 0.1
    rposibility, pos = next_token(str, pos)
    node['rp'] = rposibility
    
    # ) or name
    tmp, newpos = next_token(str, pos)
    if tmp == ')':
        pos = newpos
    else:
        rchild, newpos = feature(str, pos)
        # )
        ignore, pos = next_token(str, newpos)
        node['rc'] = rchild

    return node, pos

def root(str, pos=0):

    node = {}
    
    # (
    ignore, pos = next_token(str, pos)

    # 0.x
    posibility, pos = next_token(str, pos)
    node['p'] = posibility
    
    f, p = feature(str, pos)
    if f == None:
        return node

    node['c'] = f
    
    # )
    ignore, pos = next_token(str, pos)
    
    return node

def count(node, features):
    prob = float(node['p'])

    if 'c' not in node.keys():
        return prob

    node = node['c']
    while True:
        if node['name'] in features:
            prob *= float(node['lp'])
            if 'lc' in node.keys():  
                node = node['lc']
            else:
                break
        else:
            prob *= float(node['rp'])
            if 'rc' in node.keys():
                node = node['rc']
            else:
                break

    return prob

def main():
    t = readInts()[0]
    case = 1
    for i in range(t):
        
        n = readInts()[0]
        ss = ""
        for j in range(n):
            s = raw_input()
            ss += s

        node = root(ss)


        print 'Case #%s:' % (case)
        
        m = readInts()[0]
        for j in range(m):
            s = raw_input()
            fs = s.split()[2:]
            print '%.7f' % count(node, fs)
        

        case += 1
        
def test():
    print root('(0.2 furry  (0.81 fast    (0.3)    (0.2)  )  (0.1 fishy    (0.3 freshwater      (0.01)      (0.01)    )    (0.1)  ))')
    pass

if __name__ == '__main__':
    main()
    # test()

