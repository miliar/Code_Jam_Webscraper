
import math
test = int(input())

answer = []
for x in range(test):
    lst = input().strip().split()
    r = int(lst[0])
    c = int(lst[1])
    s = int(lst[2])

    grid = r*c
    half = (r*c)//2

    if s == 1:
        y = grid
        
    elif s == grid:
        y = s

    elif half < s:
        y = s+1

    else:
        if (grid%s) != 0:
            if (grid - (s+1)) >= s:
                y = ((grid - (s+1))//s + (s+1))
            else:
                y = s+1

        else:
            if (grid - (s)) >= s:
                y = ((grid - (s))//s + (s))
            else:
                y = s



    ans = "Case #" + str(x+1) + ": " + str(y)
    answer.append(ans)

for i in answer:
    print(i)
