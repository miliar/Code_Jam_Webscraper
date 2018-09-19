def main(argv):
    file = open('C-small-attempt0.in', 'r')
    line = file.readline()
    num = int(line[:-1])
    count = 0
    while count < num:
        line = file.readline()[:-1]
        val = str(w(line))
        print "Case #" + str(count + 1) + " " + "0"*(4-len(val)) + val
        count += 1
    

def w(str):
    count = 0
    counter = 0
    while counter < len(str):
        if str[counter] == 'w':
            count += e(str[counter:])
        counter += 1
    return count

def e(str):
    count = 0
    counter = 0
    while counter < len(str):
        if str[counter] == 'e':
            count += l(str[counter:])
        counter += 1
    return count

def l(str):
    count = 0
    counter = 0
    while counter < len(str):
        if str[counter] == 'l':
            count += c(str[counter:])
        counter += 1
    return count

def c(str):
    count = 0
    counter = 0
    while counter < len(str):
        if str[counter] == 'c':
            count += o(str[counter:])
        counter += 1
    return count

def o(str):
    count = 0
    counter = 0
    while counter < len(str):
        if str[counter] == 'o':
            count += m(str[counter:])
        counter += 1
    return count

def m(str):
    count = 0
    counter = 0
    while counter < len(str):
        if str[counter] == 'm':
            count += e2(str[counter:])
        counter += 1
    return count

def e2(str):
    count = 0
    counter = 0
    while counter < len(str):
        if str[counter] == 'e':
            count += space(str[counter:])
        counter += 1
    return count

def space(str):
    count = 0
    counter = 0
    while counter < len(str):
        if str[counter] == ' ':
            count += t(str[counter:])
        counter += 1
    return count

def t(str):
    count = 0
    counter = 0
    while counter < len(str):
        if str[counter] == 't':
            count += o2(str[counter:])
        counter += 1
    return count

def o2(str):
    count = 0
    counter = 0
    while counter < len(str):
        if str[counter] == 'o':
            count += space2(str[counter:])
        counter += 1
    return count

def space2(str):
    count = 0
    counter = 0
    while counter < len(str):
        if str[counter] == ' ':
            count += c2(str[counter:])
        counter += 1
    return count

def c2(str):
    count = 0
    counter = 0
    while counter < len(str):
        if str[counter] == 'c':
            count += o3(str[counter:])
        counter += 1
    return count

def o3(str):
    count = 0
    counter = 0
    while counter < len(str):
        if str[counter] == 'o':
            count += d(str[counter:])
        counter += 1
    return count

def d(str):
    count = 0
    counter = 0
    while counter < len(str):
        if str[counter] == 'd':
            count += e3(str[counter:])
        counter += 1
    return count

def e3(str):
    count = 0
    counter = 0
    while counter < len(str):
        if str[counter] == 'e':
            count += space3(str[counter:])
        counter += 1
    return count

def space3(str):
    count = 0
    counter = 0
    while counter < len(str):
        if str[counter] == ' ':
            count += j(str[counter:])
        counter += 1
    return count

def j(str):
    count = 0
    counter = 0
    while counter < len(str):
        if str[counter] == 'j':
            count += a(str[counter:])
        counter += 1
    return count

def a(str):
    count = 0
    counter = 0
    while counter < len(str):
        if str[counter] == 'a':
            count += m2(str[counter:])
        counter += 1
    return count

def m2(str):
    count = 0
    counter = 0
    while counter < len(str):
        if str[counter] == 'm':
            count += 1
        counter += 1
    return count

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])