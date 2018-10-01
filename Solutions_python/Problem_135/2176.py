__author__ = 'Stephane'

f = open('A-small-attempt0.in','r')
o = open('out.in','w+')

def read_grid(text):
    grid = []
    count = 0
    for line in text.rstrip('\n').split('\n'):
        grid.append(line.split(' '))
        count+=1
    print 'grid return :\n%s\n' % grid
    return  grid

def resolve(g1,g2):
    print 'g1:%s \n g2:%s\n' % (g1,g2)
    answer = []
    for n in g1:
        if n in g2:
            answer.append(n)
    return answer


grid1 = []
grid2 = []

first_line = 0
first_read = False
second_read = False
first_n = -1
second_n = -1

count = 0
case = 1
tests = 0
number = -1
for line in f.readlines():
    global text
    if first_line == 0:
        tests = line.rstrip('\r\n')
        first_line += 1
    else:
        if count < 5 and count > 0:
            text += line
            count +=1
        if count == 0:
            text = ''

            number = int(line.rstrip('\r\n'))
            print 'number %s ' % number
            count += 1
        if count == 5:

            msg = 'Case #%s: ' % case
            #print 'text\n %s\n' % text
            if first_read and not second_read:
                grid2 = read_grid(text)
                second_read = True
                second_n = number
                count = 0
                case += 1
            if not first_read:
                grid1 = read_grid(text)
                first_read = True
                first_n = number
                count = 0
            if first_read and second_read:
                first_read = False
                second_read = False
                count = 0
                print 'first : %s second : %s ' % (first_n,second_n)
                answer = resolve(grid1[first_n-1],grid2[second_n-1])
                if len(answer) == 0:
                    o.write('%sVolunteer cheated!\n'%msg)
                if len(answer) == 1:
                    o.write('%s%s\n' % (msg,answer[0]) )
                if len(answer) > 1:
                    o.write('%sBad magician!\n' % msg )
f.close()
o.close()
