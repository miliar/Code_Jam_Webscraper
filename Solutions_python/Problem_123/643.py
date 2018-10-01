from collections import deque

f = open('Google Osmos Small.in','r')
g = open('Google Osmos Small.out','w')

def Google_print(filename,answers):
    for i in range(len(answers)):
        filename.write("Case #%s: %s\n" % (str(i+1),answers[i]))
        print "Case #%s: %s" % (str(i+1),answers[i])
    return

def largest_mote(start,a):
    a.sort()
    a.reverse()
    while a:
        if start > a[-1]:
            x = a.pop()
            start += x
        else:
            break
    return start

def choose(current,array,t=0):
    a = array[:]
    a.sort()
    a.reverse()
    if not a:
        return 'done',[]
    x = largest_mote(current,a)
    a = [n for n in a if n >= x]
    if not a:
        return 'done',[]
    a1 = a[:]
    a1.append(x-1)
    answer1 = (x,a1,t+1)
    a2 = a[1:]
    answer2 = (x,a2,t+1)
    return answer1,answer2

def crunch(start,array):
    q = deque([(start,array,0)])
    while q:
        x,y,z = q.popleft()
        answer1,answer2 = choose(x,y,z)
        if 'done' in answer1 or 'done' in answer2:
            break
        else:
            q.append(answer1)
            q.append(answer2)
    return z


    


cases = int(f.readline())
answer = []
for i in range(cases):
    points,nodes = f.readline().rstrip().split(' ')
    points = int(points)
    motes = f.readline().rstrip().split(' ')
    motes = [int(x) for x in motes]
    answer.append(crunch(points,motes))

Google_print(g,answer)
f.close()
g.close()


    
    
