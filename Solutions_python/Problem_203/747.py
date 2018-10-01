#!/usr/bin/env python3

def solve(case_n, mtx):
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            letter = mtx[i][j]
            if letter != "?":
                #print("oi")
                idx = max(i - 1, 0)
                #print(idx)
                #print(mtx[0][0])
                #print("h", mtx[idx][j])
                while idx >= 0 and mtx[idx][j] == "?":
                #    print("a")
                    mtx[idx][j] = letter
                    idx -= 1
                idx = i + 1
                while idx < len(mtx) and mtx[idx][j] == "?":
                #    print("b")
                    mtx[idx][j] = letter
                    mtx[idx][j] = letter
                    idx += 1

    for __ in range(len(mtx[0])):
        for i in range(len(mtx)):
            for j in range(len(mtx[i])-1):
                letter = mtx[i][j]
                if letter == "?":
                    side = 1
                    k = i
                    while k < len(mtx) and mtx[k][j] == "?":
                        mtx[k][j] = mtx[k][j+side]
                        k += 1

    for __ in range(len(mtx[0])):
        for i in range(len(mtx)):
            for j in range(len(mtx[i])-1, 1, -1):
                letter = mtx[i][j]
                if letter == "?":
                    side = -1
                    k = i
                    while k < len(mtx) and mtx[k][j] == "?":
                        mtx[k][j] = mtx[k][j+side]
                        k += 1


    print("Case #{}:".format(case_n))
    for line in mtx:
        print("".join(line))
    #print("\n".join("".join(line for line in mtx)))

def main():
    t = int(input())
    for case_n in range(1, t+1):
        R, C = map(int, input().split(" "))
        mtx = []
        for __ in range(R):
            mtx.append(list(input()))
        solve(case_n, mtx)

if __name__ == "__main__":
    main()
