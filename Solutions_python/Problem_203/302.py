#!/usr/bin/python3
# python >= 3.6
# code jam 2017 1A  (04:00-06:30 AM GMT+3 2017-04-15)


def fill_cake(cake, R, C):
    for r in range(R):
        if cake[r].count("?") != C:
            next_letter = next(x for x in cake[r] if x != "?")
            for c in range(C):
                if cake[r][c] == "?":
                    cake[r][c] = next_letter
                else:
                    next_letter = cake[r][c]
    next_row = next(row for row in cake if row[0] != "?")
    for r in range(R):
        if cake[r][0] == "?":
            cake[r] = next_row
        else:
            next_row = cake[r]
    return(cake)
    
            

if __name__=="__main__":
    T = int(input())
    for case in range(T):
        print(f"Case #{case+1}: ")
        R, C = (int(x) for x in input().split())
        cake = list()
        for _ in range(R):
            cake.append(list(input()))
        cake = fill_cake(cake, R, C)
        for line in cake:
            print("".join(line))



    
