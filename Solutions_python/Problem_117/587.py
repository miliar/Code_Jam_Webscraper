import sys


def case(lawn,n,m):
    rows = []
    for i in range(n):
        rows.append([max(lawn[i])-lawn[i][j] for j in range(m)])
    cols = []
    for j in range(m):
        col=[lawn[i][j] for i in range(n)]
        cols.append([max(col)-col[j] for j in range(n)])
    for i in range(n):
        for j in range(m):
            if (rows[i][j] > 0) and (cols[j][i] > 0):
                print("NO")
                return
    print("YES")
    return

def work(fin):
    t = int(fin.readline())
    for i in range(t):
        lawn = []
        print("Case #",i+1,": ",end="",sep="")
        temp = fin.readline().split()
        n,m = int(temp[0]),int(temp[1])
        for j in range(n):
            lawn.append(list(map(int, fin.readline().strip().split())))
        case(lawn,n,m)

if __name__ == "__main__":
    INPUT = sys.argv[1]

    fin = open(INPUT,'r')
    work(fin)
