
def tidy(mx):
    for l in range(mx, 0, -1):
        a = str(l)
        b = list(str(l))
        b = "".join(sorted(b))
        if a==b:
            return l
            

for case in range(int(input())):
    case+=1
    mx = int(input())
    print("Case #"+str(case)+": "+str(tidy(mx)))