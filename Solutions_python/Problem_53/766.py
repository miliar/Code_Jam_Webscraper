import sys

fin = open("A-small-attempt1.in","r")
fout = open("snapper_small.out","w")

t = int(fin.readline().strip())
for i in range(t):
        nums = fin.readline().strip().split()
        N = int(nums[0])
        K = int(nums[1])
        num_snaps = (2**N)
        if(K==0):
                #print "Case #" + str(i+1) + ": OFF\n"
                fout.write("Case #" + str(i+1) + ": OFF\n")
        else:
                if(((K+1)%num_snaps) == 0):
                        #print "Case #" + str(i+1) + ": ON\n"
                        fout.write("Case #" + str(i+1) + ": ON\n")
                else:
                        #print "Case #"+ str(i+1) + ": OFF\n"
                        fout.write("Case #"+ str(i+1) + ": OFF\n")

fout.close()
fin.close()


            
    
    


