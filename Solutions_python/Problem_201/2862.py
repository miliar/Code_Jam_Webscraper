def stalls(n, k):
    occupied = [0] * n
    occupied.append(1)
    occupied.insert(0, 1)
    for i in range(k):
        values = {}
        for j in range(len(occupied)):
            if not occupied[j]:
                ls = 0
                ix = j - 1
                while not occupied[ix]:
                    ix -= 1
                    ls += 1
                rs = 0
                ix = j + 1
                while not occupied[ix]:
                    ix += 1
                    rs += 1
                values[j] = (min(ls,rs),max(ls,rs))
        #pick stall
        mi = -1
        ma = -1
        pick = 0
        stalls = sorted(values.keys(), reverse=True)
        for s in stalls:
            val = values[s]
            if val[0] > mi:
                mi = val[0]
                ma = val[1]
                pick = s
            if val[0] == mi:
                if val[1] >= ma:
                    ma = val[1]
                    pick = s

        occupied[pick] = 1
        
        if i == k-1:
            print(str(values[pick][1]) + " " + str(values[pick][0]))
 
t = int(input())

for i in range(1, t + 1):
    print("Case #" + str(i) + ": ", end="")
    line = input().split(" ")
    stalls(int(line[0]), int(line[1]))

                
        
