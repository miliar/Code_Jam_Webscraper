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
        isInOrder=True
        currentCase=currentCase+1
        number=str(int(line))
        for i in range(0,(len(number)-1)):
            if(number[i]>number[i+1]):
                #not yet in order
                isInOrder=False
                break
        if(isInOrder):
            output.write("Case #"+ str(currentCase)+": "+ number+"\n")
        else:
            leng=len(number)
            number=list(map(int, list(number)))
            for i in range(leng-2,-1,-1):
                    while(number[i]>number[i+1]):
                        number[i]=number[i]-1
                        if(number[i]==-1):
                            number[i]=0
                        for j in range (i+1, leng):
                            number[j]=9
            
            number = map(str, number)   # ['1','2','3']
            number = ''.join(number)          # '123'
            number = int(number)
            output.write("Case #"+ str(currentCase)+": "+ str(number)+"\n")
                

if __name__ == '__main__':
    main()