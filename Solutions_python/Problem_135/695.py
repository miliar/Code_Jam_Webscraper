for t in xrange(1,input()+1):
    g1 = input()
    mat1 = [raw_input() for i in xrange(4)][g1-1].split()
    g2 = input()
    mat2 = [raw_input() for i in xrange(4)][g2-1].split()
    inter = [x for x in mat1 if x in mat2]
    answer = inter[0] if len(inter)==1 else 'Volunteer cheated!' if len(inter)==0 else 'Bad magician!'
    print 'Case #'+str(t)+': '+answer
