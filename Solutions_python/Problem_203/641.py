import sys

def caked(cake):
    caked = [[ch for ch in row] for row in cake]
    #print(caked)
    #kids = []

    #print(caked)
    for i, row in enumerate(caked):
        #forward pass
        kern = '?'
        for j, piece in enumerate(row):
            if piece != '?':
                kern = piece
            if piece is '?':
                caked[i][j] = kern
        for j, piece in enumerate(reversed(row)):
            if piece != '?':
                kern = piece
            if piece is '?':
                caked[i][-(j+1)] = kern
        if i > 0:
            for j, piece in enumerate(row):
                if piece == '?':
                    caked[i][j] = caked[i-1][j]
    for i, row in enumerate(reversed(caked)):
        if i > 0:
            for j, piece in enumerate(row):
                if piece == '?':
                    caked[-(i+1)][j] = caked[-i][j]
    #print(caked)
    return [''.join(row) for row in caked]


def main():
    with open(sys.argv[1], 'r') as infile:
        for i, line in enumerate(infile):
            if i == 0:
                continue
            rows, cols = line.strip().split()
            cake = [next(infile).strip() for _ in range(0,int(rows))]
            divcake = caked(cake)
            print("Case #" + str(i) + ":")
            for row in divcake:
                print(str(row))

if __name__ == "__main__":
    main()