def nueves(rang):
    return ''.join(['9' for i in range(rang)])

def solve():
    string = input()
    if(len(string)==1):
        return string
    i=0
    while(i<len(string)-1):
        #print(i)
        i = max(0,i)
        if(string[i]>string[i+1]):
            string = string[0:i]+str(int(string[i])-1)+nueves(len(string)-(i+1))
            #print(string)
            i-=2
        i+=1
        
            
    return int(string)

def main():
    t = int(input())
    for i in range(t):
        print("Case #"+str(i+1)+": "+str(solve()))
main()
