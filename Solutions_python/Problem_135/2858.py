import sys
sys.stdin = open('A-small-attempt0.in')
sys.stdout = open('A-small-attempt0.out', 'w')
#myout = open('myoutput.out')

for t in range(1, input()+1):
    a1 = input()
    for i in range(1, a1):
        raw_input()
    n1 = [int(n) for n in raw_input().strip().split(' ')]
    for i in range(a1+1, 5):
        raw_input()
    a2 = input()
    for i in range(1, a2):
        raw_input()
    n2 = [int(n) for n in raw_input().strip().split(' ') if int(n) in n1]
    for i in range(a2+1, 5):
        raw_input()
    print 'Case #' + str(t) + ':',
    if len(n2) == 0:
        print 'Volunteer cheated!'
    elif len(n2) == 1:
        print n2[0]
    else:
        print 'Bad magician!'
