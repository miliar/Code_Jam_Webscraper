import fileinput

f = fileinput.input()

T = int(f.readline())

for case in range(0,T):
    line=(f.readline())
    N=len(line)
    N=N-1;
    flag=0;
    # print "length"+ str(N)
    while(flag != 1):
        if(int(line)==1 or N==1):
            # line=int(line)
            flag=1;
            break;
        else:
            for i in range (0,N-1):
                    # print "i"+ str(i)
                    if(line[i] <= line[i+1]):
                        # print line[i] +"   "+ line[i+1]
                        flag=1;
                        # if(i== N-1):
                        #     break;
                    else:
                        # print "esle"+ line
                        line=int(line)-1;
                        line=str(line)
                        N = len(line)
                        # print str(N)+ "esle" + line
                        flag=0;
                        break;

    print 'Case #' + str(case+1) + ': ' + str(int(line))







