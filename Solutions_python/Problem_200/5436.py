#T = input()
my_file=open('Test.txt','r')
#List = []
#for i in range (0,int(T)):
    #N = input()
    ##Del=Word.split()
    #List.append(N)
List=my_file.readlines()
my_file.close()

R=[]
s=1
for i in List:
    if int(i)<10:
        R.append('Case'+' '+'#'+str(s)+':'+' '+i)
        #print('Case'+' '+'#'+str(s)+':'+' '+i)
    if int(i)>=10: #and int(i[0])!=1:
        Y=i
        Y=Y[1:len(i)+1]
        X=int(i)-int(Y)-1
        Word=X
        for j in range (int(i),X-1,-1):
            A=str(j)
            p=0
            for k in range(0,len(A)-1):
                if int(A[k])<=int(A[k+1]):
                    p=p+1
            if p==len(A)-1:
                Word=A
                break
        R.append('Case'+' '+'#'+str(s)+':'+' '+Word)
        #print('Case'+' '+'#'+str(s)+':'+' '+Word)
    s=s+1

my_file=open('Result.txt','w')

for i in R:
    my_file.write(i+'\n')
my_file.close()