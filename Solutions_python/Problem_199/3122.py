from sys import stdin
def solve(s,k,n,h):
    for i in range(len(s)):
        if s[i]=="-":
            if i+k<=len(s):
                n+=1
                for j in range(i,i+k):
                    if s[j]=="+":
                        s[j]="-"
                    else:
                        s[j]="+"
            else:
                print("Case #"+str(h+1)+": IMPOSSIBLE")
                return
        
    print("Case #"+str(h+1)+":",n)
    return
def main():
    for h in range(int(stdin.readline())):
        s,k=stdin.readline().strip().split()
        s=list(s)
        k=int(k)
        n=0
        if "-" not in s:
            print("Case #"+str(h+1)+":",0)
        else:
            solve(s,k,n,h)
            
main()
