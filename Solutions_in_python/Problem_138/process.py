def solve(R, C, M): 
    NM = R*C-M;   
    if M==0:
        board = [['.' for i in range(C)] for j in range(R)]
        board = [''.join(l) for l in board]
        return "\n".join(board)
    if NM==1:
        board = [['*' for i in range(C)] for j in range(R)]
        board[0][0] = 'c'
        board = [''.join(l) for l in board]
        return "\n".join(board)
    if R==1:
        return ''.join(['c']+['.' for i in range(C-M-1)]+['*' for i in range(M)])
    if C==1:
        return '\n'.join(['c']+['.' for i in range(R-M-1)]+['*' for i in range(M)])
    if NM<=3:
        return 0
    if R==2 or C==2:
        if (M%2)==1:
            return 0
        if R==2:
            board = [['.' for i in range(C-M/2)]+['*' for i in range(M/2)] for j in range(R)]
            board[0][0] = 'c'
            board = [''.join(l) for l in board]
            return "\n".join(board)
        if C==2:
            board = ['c.']+['..' for j in range(R-M/2-1)]+['**' for j in range(M/2)]
            return "\n".join(board)
    if NM==5 or NM==7:
        return 0
    rows = NM/C;
    excess = NM%C;
    if rows>=2:
        if excess!=1:
            board =[['.' for i in range(C)] for j in range(rows)]+[['.' for i in range(excess)]+['*' for i in range(C-excess)]]+ [['*' for i in range(C)] for j in range(R-rows-1)]
        else:
            if rows==2:
                board =[['.' for i in range(C-1)]+['*'] for j in range(2)]+[['.' for i in range(3)]+['*' for i in range(C-3)]]+[['*' for i in range(C)] for j in range(R-rows-1)]
            else:    
                board =[['.' for i in range(C)] for j in range(rows-1)]+[['.' for i in range(C-1)]+['*']]+[['.' for i in range(2)]+['*' for i in range(C-2)]]+ [['*' for i in range(C)] for j in range(R-rows-1)]
    else:
        if NM%2==0:
            board =[['.' for i in range(NM/2)]+['*' for i in range(C-NM/2)] for j in range(2)]+[['*' for i in range(C)] for j in range(R-2)]
        else:
            board =[['.' for i in range((NM-3)/2)]+['*' for i in range(C-(NM-3)/2)] for j in range(2)]+[['.' for i in range(3)]+['*' for j in range(C-3)]]+[['*' for i in range(C)] for j in range(R-3)]
    board[0][0] = 'c'
    board = [''.join(l) for l in board]
    return "\n".join(board)  
        

f_in = open('D-large.in', 'r')
f_out = open('D-large.out', 'w')

T = int(f_in.readline())
for case_id in range(T):
    C = int(f_in.readline().strip())
    N = [float(x) for x in f_in.readline().strip().split()]
    K = [float(x) for x in f_in.readline().strip().split()]
    N.sort(reverse = True); K.sort(reverse = True);
    honest_count = 0;
    Nh = N[:]; Kh = K[:];
    while Nh:
        if Nh[0]>Kh[0]:
            honest_count+=1;
            Nh.pop(0)
            Kh.pop(-1)
        else:
            Nh.pop(0)
            Kh.pop(0)
    Nd = N[:]; Kd = K[:];
    d_count = 0;
    for n in Nd:
        if n<Kd[-1]:
            break
        for k_i, k in enumerate(Kd):
            if k<n:
                Kd.pop(k_i)
                d_count+=1
                break
    f_out.write('Case #'+str(case_id+1)+': '+str(d_count)+' '+str(honest_count)+ '\n')
            
            
#            print out
#    if out==0:
#        f_out.write('Impossible\n')
#    else:
#        f_out.write(out+'\n')

    