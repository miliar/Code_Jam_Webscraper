# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.

T = int(raw_input())  # number of cases
for i in xrange(1, T + 1):
    N=str(int(raw_input())) # last number counted by Tatiana
    N=list(N)
    j=0
    stop=False
    digits=['-']*10 # the ith position of this list indicates the first appearence of the digit i on the number N
    digits[int(N[0])]=0
    while j < len(N)-1 :
        if N[j+1] != N[j] :
            digits[int(N[j+1])]=j+1
        if int(N[j+1]) < int(N[j]) :
            j=int(digits[int(N[j])])
            N[j]=str(int(N[j])-1)
            stop=True
            j+=1
            break
        j+=1
    while stop and j < len(N) :
        N[j]='9'
        j+=1
    print "Case #"+str(i)+": "+str(int(''.join(N)))

            

