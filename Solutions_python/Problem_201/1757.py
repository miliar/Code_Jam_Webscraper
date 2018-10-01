import sys

def stall(string):
    n, k = [int(x) for x in string.split()]
    n = n - 1 #for 0 indexed length
    #for each empty stall s, compute ls and rs empty stalls left and right
    ls = int(n/2)
    rs = n - ls
    #print(ls, rs)
    splits = [ls,rs]
    for i in range(1, k):
        #get index of next stall
        ind = splits.index(max(splits))
        #get next split and place
        n = splits.pop(ind) - 1
        ls = int(n/2)
        rs = n - ls
        splits.insert(ind, ls)
        splits.insert(ind+1, rs)
    if ls < 0: ls = 0
    if rs < 0: rs = 0
    return str(max(ls,rs)) + " " + str(min(ls,rs))
    #find max(min(ls,rs)) -> fill
     #if multiple, find max(max(ls,rs)) -> fill
      #if multiple, choose leftmost
    #return last max(ls,rs) and min(ls,rs)

def main():
    with open(sys.argv[1], 'r') as infile:
        for i, line in enumerate(infile):
            if i == 0:
                continue
            print("Case #" + str(i) + ": " + str(stall(line.strip())) )

if __name__ == "__main__":
    main()