from collections import deque
test_file_name = 'A-large'
f = open(test_file_name + '.in', 'r')
fw = open(test_file_name + '.out', 'w')
T = int(f.readline())
for case in range(1,T+1):
    #print(i)
    
    line = f.readline()
    line = line.split()
    line.reverse()

    # count of elements
    N = int(line.pop())

    # read data
    O, B = [], []   #work duration
    pO, pB = [], [] #priority: from 0 to N-1, 0 is the first
    o_pos, b_pos = 1, 1
    for idx in range(0, N):
        robot = line.pop()
        position = int(line.pop())
        if( robot == 'O' ):
            O.append( int(abs(position-o_pos)+1) )
            pO.append( idx )
            o_pos = position
        elif( robot == 'B' ):
            B.append( int(abs(position-b_pos)+1) )
            pB.append( idx )
            b_pos = position
    # the last input is the first to use
    O.reverse()
    B.reverse()
    pO.reverse()
    pB.reverse()
    # end read data

    # data process
    ans = 0
    while( len(O) != 0 and len(B) != 0 ):
        o, po = O.pop(), pO.pop()
        b, pb = B.pop(), pB.pop()
        if( po < pb ):
            ans += o
            if( b >= o + 1 ):
                b-=o
            else:
                b=1
            pB.append(pb)
            B.append(b)
        elif( pb < po ):
            ans += b
            if( o >= b + 1 ):
                o-=b
            else:
                o=1
            pO.append(po)
            O.append(o)
    if( len(O) == 0 ):
        ans += sum(B)
    elif( len(B) == 0 ):
        ans += sum(O)
    # end data process

    # result representation
    
    #print(ans)
    output = 'Case #' + str(case) +': ' + str(ans)
    print(output)

    fw.write(output + '\n')

    # end result representation

f.close()
fw.close()
