import sys                       
import os

def main():
    s = ''.join(sys.stdin.readlines()).split()
    os.close(0)

    T = int(s[0])
    s = s[1:]

    for i in range(T):
        N = int(s[0])
        s = s[1:]
        wires = []
        for j in range(N):
            wires += [(int(s[0]),int(s[1]))]
            s = s[2:]
        count = 0
        for j in range(N):
            for k in range(j, N):
                if (wires[j][0] > wires[k][0] and wires[j][1] < wires[k][1]) or (wires[j][0] < wires[k][0] and wires[j][1] >  wires[k][1]):
                    count += 1
        print "Case #" + str(i+1) + ": " + str(count)


if __name__ == "__main__":
 	main()

