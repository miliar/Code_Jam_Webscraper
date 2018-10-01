#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Madushan
#
# Created:
# Copyright:   (c) Madushan
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    inf = open("1.in","r")
    ouf = open("1.out","w")
    tc = int(inf.readline())
    count = 0
    j=0
    for i,line in enumerate(inf):
        if i%10==0 and i!=0:
            count+=1
            j=0

        if i == count*10:
            k=int(line)
            #print(k)
        if i == count*10+k:
            line1=[int(x) for x in line.split()]
            #print("tc",count,"line",k,line1)
        if i == count*10+5:
            j=int(line)
            #print(j)
        if j!=0 and i == count*10+5+j:
            line2=[int(x) for x in line.split()]
            #print(line2)
            #print("tc",count,"line",j,line2)
            z = set(line1) & set(line2)
            if(len(z)==0):
                ouf.write("Case #"+str(count+1)+": Volunteer cheated!\n")
            elif(len(z)>1):
                ouf.write("Case #"+str(count+1)+": Bad magician!\n")
            else:
                ouf.write("Case #"+str(count+1)+": "+str(z.pop())+"\n")
    inf.close()
    ouf.close()

if __name__ == '__main__':
    main()
