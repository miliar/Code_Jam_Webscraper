def solve(lines):
    AC = int(lines[0].split(" ")[0])
    AJ = int(lines[0].split(" ")[1])
    C = [(int(line.split(" ")[0]),int(line.split(" ")[1])) for line in lines[1:1+AC]]
    J = [(int(line.split(" ")[0]),int(line.split(" ")[1])) for line in lines[1+AC:]]
    
    ctime=0
    jtime=0
    
    if AC+AJ==1:
        return str(2)
    
    if AC == 0:
        J = sorted(J, key = lambda x:x[0])
        #print J
        
        empty1 = J[1][0] - J[0][1]
        empty2 = J[0][0]+1440-J[1][1]
        if empty1>=720 or empty2>=720:
            return str(2)
        else:
            return str(4)
        #print empty1, empty2
    elif AC == 1:
        ctime = J[0][1]-J[0][0]
        jtime = C[0][1]-C[0][0]
        return str(2)
    elif AC == 2:
        C = sorted(C, key = lambda x:x[0])
        empty1 = C[1][0] - C[0][1]
        empty2 = C[0][0]+1440-C[1][1]
        
        if empty1>=720 or empty2>=720:
            return str(2)
        else:
            return str(4)
        #print C
		
		
import sys
filename = sys.argv[1]
f = open(filename, "r")
s = f.read()
f.close()


lines = s.split("\n")
lines = [l.strip() for l in lines]
T = int(lines[0])
j=1
for i in range(1,T+1,1):
	l = lines[j]
	R = int(l.split(" ")[0]) + int(l.split(" ")[1])
	IN = lines[j:j+1+R]
	j+=R+1
	ans = solve(IN)
	print "Case #"+str(i)+": "+ans