t = int(raw_input())

for j in range(t):
    n, k = raw_input().split()
    n = int(n)
    k = int(k)

    if n == k:
        y = 0
        z = 0
        print "Case #{0}: {1} {2}".format(j+1, y, z)
    else:
        occupied = [False for i in range(n+2)]
        occupied[0] = True
        occupied[n+1] = True

        last_max, last_min = None, None
        for i in range(k):
            selected = []
            for o in range(n+2):
                if occupied[o]:
                    continue
                left = 0
                while not occupied[o-1-left]:
                    left += 1
                right = 0
                while not occupied[o+1+right]:
                    right += 1
                if not selected or selected[0][1] == min(left, right):
                    selected.append((left if left > right else right, right if right < left else left, o))
                elif selected[0][1] < min(left, right):
                    selected = [(left if left > right else right, right if right < left else left, o)]
            last_min = selected[0][1]
            if len(selected) == 1:
                occupied[selected[0][2]] = True
                last_max = selected[0][0]
            else:
                y, o = selected[0][0], selected[0][2]
                for s in range(len(selected)):
                    if selected[s][0] > y:
                        y = selected[s][0]
                        o = selected[s][2]
                occupied[o] = True
                last_max = y
        print "Case #{0}: {1} {2}".format(j+1, last_max, last_min)
