__author__ = 'duo 11'
File = open("A-large.in","r")
Out = open("output.out","w")
T = int(File.readline().replace("\n",''))

for z in xrange(T):
    N, State = File.readline().replace("\n",'').split(' ')
    Add = 0
    Total_Add = 0
    Total = 0
    for i in xrange(int(N) + 1):
        if Total >= i: Total += int(State[i])
        else:
            Add = i - Total
            Total = Total + Add + int(State[i])
            Total_Add += Add
    Out.write("Case #" + str(z+1) + ": " + str(Total_Add) + "\n")
Out.close()
