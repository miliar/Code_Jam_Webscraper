import sys


def read_input():
    with open("random.txt") as f:
        T = int(f.readline().strip('\n'))
        for i in xrange(1, T + 1):
            N = int(f.readline().strip('\n'))
            P = N
            while N >= 0:
                digits_list = list(str(N))
                res = True
                l = len(digits_list)
                for j in range(l-1):
                    if digits_list[j] > digits_list[j+1]:
                        res = False
                        break
                if res == False:
                    N= N-1
                    continue
                else:
                    print "Case #{}: {}".format(i, N)
                    break


def main():
    read_input()

if __name__ == '__main__':
    main()