
def main():
    fin = open('C:\Users\Administrator\Desktop\A-small-attempt1.in', 'r')
    fout = open('C:\Users\Administrator\Desktop\output.txt', 'w')
    T = int(fin.readline())
    for t in xrange(1, T+1):
        p, q = map(int, fin.readline().split('/'))
        if q & (q - 1) != 0:
            fout.write("Case #" + str(t) + ": impossible\n")
            continue
        res = 1
        while p != q and res <= 40:
            if 2 * p - q < 0:
                p *= 2
                res += 1
            else:
                break
        if res <= 40:
            fout.write("Case #" + str(t) + ": " + str(res) + "\n")
        else:
            fout.write("Case #" + str(t) + ": impossible\n")
    fin.close()
    fout.close()

if __name__ == '__main__':
    main()