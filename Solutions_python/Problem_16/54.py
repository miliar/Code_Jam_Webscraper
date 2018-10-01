# Task X
# Written in Python

testing = False

import sys

def perms(combo):
   if combo == []:
       return [[]]
   return [[combo[i]] + p
     for i in range(len(combo))
     if i == combo.index(combo[i])
     for p in perms(combo[:i]+combo[i+1:])]    

def perm(data):
    length, string = data
    length = int(length)
    combos = perms(range(length))
    minimum = sys.maxint
    for combo in combos:
        changed = ''
        for i in range(len(string)/length):
            for j in range(length):
                changed += string[i*length+combo[j]]
        count = 1
        previous = changed[0]
        for char in changed:
            if previous != char:
                previous = char
                count += 1
        if count < minimum:
            minimum = count
    return minimum

def main():
    if testing:
        file_name = 'D-test'
    else:
        file_name = raw_input('Enter file: ')
    try:
        f = open(file_name + '.in', 'rU')
    except:
        print 'File "' + file_name + '.in" does not exist!'
    else:
        inputs = ''
        data = []
        for line in f:
            inputs += line
            if line.strip('\n') != '':
                data.append(line.strip('\n'))
        f.close()
        output = []
        count = int(data[0])
        for i in xrange(1, count+1):
            output.append('Case #%s: %s' % (i, perm([data[i*2-1],data[i*2]])))
        output = '\n'.join(output)
        if testing:
            print output
        else:
            print inputs
            print output
            f = open(file_name + '.out', 'w')
            f.write(output)
            f.close()

main()
