## This solutions takes a number and finds the digit before it which is well orderd

def magic (n, ctr):
    k = list(str(n))
    for i in range(len(k)-1, 0, -1):
        if k[i-1] > k[i]:
            k[i-1] = str(int(k[i-1]) -1)
            k[i:] = [ "9" for j in range(i,len(k))]
    st = "".join(k)
    b = int(st)
   ## print(int(st))
    print("Case #" + str(ctr) + ": " + str(b))

def main():
    ctr = 0
    for i in range(int(input())):
        ctr += 1
        magic(int(input()),ctr)


if __name__ == "__main__":
    main()
