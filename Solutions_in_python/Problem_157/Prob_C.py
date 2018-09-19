__author__ = 'duo 11'

Map = [[0,1,2,3],
       [1,0,3,2],
       [2,3,0,1],
       [3,2,1,0]]

Plus = [[0,0,0,0],
        [0,1,0,1],
        [0,1,1,0],
        [0,0,1,1]]
#File = open("small.in","r")
File = open("C-small-attempt1.in","r")
Out = open("C-output.out","w")
T = int(File.readline().replace("\n",''))

for z in xrange(T):
    N, M = File.readline().replace("\n",'').split(' ')
    N, M = int(N), int(M)
    Line = File.readline().replace("\n",'').replace('i','1').replace('j','2').replace('k','3')

    Result = 0
    Moss = 0

    idx = 0
    R_Count = 0
    Finding = [1,2]
    STEP = 0
    while R_Count != M:
        K = int(Line[idx])
        Moss += Plus[Result][K]
        Result = Map[Result][K]

        idx = idx + 1
        if idx == N:
            idx = 0
            R_Count += 1
        if STEP < 2 and Result == Finding[STEP] and Moss % 2 == 0:
            STEP += 1
            Result = 0

    if STEP == 2 and Result == 3 and Moss % 2 == 0:
        Out.write("Case #" + str(z+1) + ": " + "Yes" + "\n")
    else:
        Out.write("Case #" + str(z+1) + ": " + "No" + "\n")