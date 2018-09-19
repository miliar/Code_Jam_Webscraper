def count(line):
    d = {}
    first_flag = True
    second_flag = True
    for i in line:
        if i in d.keys():
            continue
        else:
            if first_flag == True: # the first bit is 1
                d[i] = 1
                first_flag = False
            elif second_flag == True:
                d[i] = 0
                second_flag = False
            else:
                d[i] = max(d.values()) + 1
    return d

def translate(line):
    tmp = ''
    d = count(line)
    for i in line:
        tmp = tmp + str(d[i])
    base = 0
    if (len(d.keys()) > 1):
        base = len(d.keys())
    else:
        base = 2
    return (tmp, base)

def get_number(s, base):
    s = [i for i in s]
    s.reverse()
    r = 0
    for i in range(len(s)):
        r = r + int(s[i])*(base**i)
    return r

def doit(line):
    s, base = translate(line)
    return get_number(s, base)
