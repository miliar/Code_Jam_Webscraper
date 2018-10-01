import sys

if __name__ == "__main__":

    sys.stdin = open('A-small-attempt2.in', 'r')
    sys.stdout = open('A-small-attempt2.out', 'w')

    for c in range(int(input())):
        (m, x) = map(str, input().split())
        m = int(m)
        iv = 0
        count = 0
        for i in range(m+1):
            if(i == 0):
                count = int(x[i])
            else:
                if (count >= i):
                    count += int(x[i])
                elif (int(x[i]) != 0):
                    iv += i-count
                    count += (iv+int(x[i]))
        print('Case #%d: %d' %(c+1, iv))

    sys.stdin.close()
    sys.stdout.close()
