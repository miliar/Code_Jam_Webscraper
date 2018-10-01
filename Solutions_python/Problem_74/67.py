name = "A-large"
f_in = open(name + '.in',"r")
f_out = open(name + '.out','w')

def calc(l1,l2,po,pb,mo,mb):
        if(len(l1) == 0):
                return 0
        else:
                if(l2[0] == 'O'):
                        m = abs(l1[0] - po)
                        if(m>=mo):
                                return calc(l1[1:],l2[1:],l1[0],pb,0,mb+m-mo+1) + m - mo + 1
                        else:
                                return calc(l1[1:],l2[1:],l1[0],pb,0,mb+1) + 1
        
                elif(l2[0] == 'B'):
                        m = abs(l1[0] - pb)
                        if(m>=mb):
                                return calc(l1[1:],l2[1:],po,l1[0],mo+m-mb+1,0) + m - mb + 1
                        else:
                                return calc(l1[1:],l2[1:],po,l1[0],mo+1,0) + 1

T  =  int(f_in.readline())
for i in range(T):
        l = [x for x in (f_in.readline().split())]
        l1 = [int(l[x]) for x in range(2,len(l),2)]
        l2 = [l[x] for x in range(1,len(l),2)]
        print(l1)
        print(l2)
        f_out.write("Case #" +str(i+1) + ": "+ str(calc(l1,l2,1,1,0,0))+"\n")

 

f_in.close()
f_out.close()
