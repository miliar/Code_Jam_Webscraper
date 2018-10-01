f = open('D-small-attempt2.in')
#f = open('test.in')
count = int(f.readline())
output = ''
for i in xrange(1, count + 1):
    arr = f.readline().split()
    X = int(arr[0])
    R = int(arr[1])
    C = int(arr[2])
    square = R * C
    if square % X != 0:
        output += 'Case #' + str(i) + ': RICHARD\n'
    elif square / X < (X - 1):
        output += 'Case #' + str(i) + ': RICHARD\n'
    else:
        output += 'Case #' + str(i) + ': GABRIEL\n'


print(output)
newf = open('output.txt','w')
newf.write(output)
