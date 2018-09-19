f = open('B.txt')
lines = f.readlines()
f.close()
def is_power2(num):

    #'states if a number is a power of two'
    
    return num != 0 and ((num & (num - 1)) == 0)

output = open('BOutput.txt','w')
for i in range(int(lines[0])):
    var = lines[i+1].split()
    A = int(var[0]) - 1
    B = int(var[1]) - 1
    Acop = A
    Bcop = B
    K = int(var[2])
    ways = 0
    while(A >= 0):
        while(B >= 0):
            winning = A&B
            if(winning < K):
                ways += 1
            B -= 1
        B = Bcop
        A -= 1
        
    print B 
    print K
    output.write("Case #" + str(i+1) + ": ")
    output.write(str(ways))
    output.write("\n")
output.close() 
