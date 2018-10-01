'''
Created on Apr 8, 2017

@author: morettini
'''

def main():
    input=open('input.txt', 'r')
    output=open('output.txt', 'w')
    Tcases=input.readline()
    currentCase=0
    
    for line in input:
        currentCase=currentCase+1
        exchange=0
        lis=line.split(' ')
        seqL=list(lis[0])
        dim=int(lis[1])
        for i in range(0,len(seqL)-dim+1):
            if(seqL[i]=='-'):
                exchange=exchange+1
                for j in range (0,dim):
                    seqL[i+j]='+' if seqL[i+j]=='-' else '-'
        for i in range(0,len(seqL)):
            if(seqL[i]=='-'):
                output.write("Case #"+ str(currentCase)+": IMPOSSIBLE \n")
                break
        else:
            output.write("Case #"+ str(currentCase)+": "+str(exchange)+ "\n")
       


if __name__ == '__main__':
    main()