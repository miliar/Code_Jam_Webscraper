import sys

if __name__ == '__main__':
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)
    output = open('jam1.out', 'w')
    t = int(f.readline())
    for test in xrange(1, t+1):
        str1 = "Case #%d: " %(test)
        output.write(str1)
        x = int(f.readline())
        arr1 = []
        for i in range(4):
            line = map(int, f.readline().split())
            arr1.append(line)
        y = int(f.readline())
        arr2 = []
        for j in range(4):
            line = map(int, f.readline().split())
            arr2.append(line)
        cnt = 0
        ans = -1
        for i in range(4):
            for j in range(4):
                if arr1[x-1][i] == arr2[y-1][j]:
                    ans = arr1[x-1][i]
                    cnt += 1
        if cnt == 0:
            output.write("Volunteer cheated!\n")
        elif cnt == 1:
            output.write(str(ans) + "\n")
        else:
            output.write("Bad magician!\n")
