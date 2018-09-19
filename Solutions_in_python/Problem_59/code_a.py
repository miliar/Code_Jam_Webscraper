f = file('d:/jam/A-large.in')
fw = file('d:/jam/outal.txt', 'w')
T = int(f.next())

for i in range(T):
    N,M = [int(x) for x in f.next().split(' ')]

    folder = set()

    for ii in range(N):
        s = f.next()[1:-1]


        ss = s.split('/')
        #del ss[0]

        sofar = ''

        for iii in range(len(ss)):
            sofar += '/' + ss[iii]
            folder.add(sofar)
         #   
    #N

    #print folder
    res = 0

    for ii in range(M):
        s = f.next()[1:-1]
        ss = s.split('/')

        
        #del ss[0]

        sofar = ''
        #print '%d @ %s  [%s]'  % (res,s, str(ss))
                
        for iii in range(len(ss)):
            sofar += '/' + ss[iii]
            if sofar not in folder:
                folder.add(sofar)
                res+=1
        #
    #print 'Case %d: %d' % (i+1, res)
    fw.write('Case #%d: %d\n' % (i+1, res)   )

    #break
    #if i == 1: break
#
f.close()
            
        

fw.close()
