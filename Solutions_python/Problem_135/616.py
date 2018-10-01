import sys

def main():
    infile, outfile = sys.argv[1:3]
    with open(infile, 'r') as inp:
      with open(outfile, 'w') as out:
        T = int(inp.readline())
        for case in range(1, T+1):
            r1 = int(inp.readline())
            sq1 = []
            for r in range(4):
                sq1.append([int(i) for i in inp.readline().split()])
            r2 = int(inp.readline())
            sq2 = []
            for r in range(4):
                sq2.append([int(i) for i in inp.readline().split()])
            common = [item for item in sq1[r1-1] if item in sq2[r2-1]]
            k = len(common)
            if k == 1:
                ans = str(common[0])
            elif k == 0:
                ans = "Volunteer cheated!"
            else:
                ans = "Bad magician!"

            out.write('Case #{}: '.format(case))
            out.write('{}\n'.format(ans))

if __name__ == '__main__':
    main()
