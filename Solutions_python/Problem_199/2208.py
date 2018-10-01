def flip(s):
    if s == "-":
        return "+"
    else:
        return "-"

def magic(l, k):
    ctr = 0;
    for i in range(len(l)-k+1):
        if l[i] == "-":
            ctr += 1
            for j in range(k):
                l[i +j] = flip(l[i+j])
    #print(l)
    for i in range(1, k):
        #print(i, len(l)-i, l[len(l)-i])
        if l[len(l)-i] == "-":
            return "IMPOSSIBLE"
    return str(ctr)
        

def main():
    ctr = 0
    for t in range(int(input())):
        ctr += 1
        a = raw_input().split()
        ret =  magic(list(a[0]), int(a[1]))
        print("Case #" + str(ctr) + ": " + ret)
        


if __name__ == "__main__":
    main()
