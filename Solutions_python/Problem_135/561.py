T=int(raw_input())
for case in range(T):
    print "Case #%d:"%(case+1),
    a=int(raw_input())
    for i in range(1,5):
        s=raw_input()
        if i==a:
            p=set(s.split(' '))
    b=int(raw_input())
    for i in range(1,5):
        s=raw_input()
        if i==b:
            q=set(s.split(' '))
    res=p&q
    if(len(res)==1):
        print int(tuple(res)[0])
    elif len(res)==0:
        print 'Volunteer cheated!'
    else:
        print 'Bad magician!'

