from sys import stdin
def solve(n):
    lista= list(str(n))
    listacopy= lista.copy()
    listacopy.sort()
    if lista==listacopy:
        
        return n
    for i in range(len(lista)-1):
        
        if int(lista[i])>int(lista[i+1]):
            
            lista[i]=str(int(lista[i])-1)
            if lista[i]=="0":
                return "9"*(len(lista)-1)
            lista= lista[:i+1]+(["9"]*(len(lista)-i-1))
            listacopy= lista.copy()
            listacopy.sort()
            if lista!=listacopy:
                return solve(int("".join(lista)))
            return "".join(lista)
        
def main():
    cases=  int(stdin.readline().strip())
    for i in range(cases):
        n= int(stdin.readline().strip())
        if 0<=n<=9:
            print("Case #"+str(i+1)+": "+str(n))
        else:
            print("Case #"+str(i+1)+": "+str(solve(n)))
main()
