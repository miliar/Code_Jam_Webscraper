t = int(input())

for test_num in range(1, t+1):
    ans = ''
    n, k = map(int, input().split())

    rooms = [False] * (n+2)
    rooms[0] = True
    rooms[-1] = True

    #print(rooms)

    min_score = 0
    max_score = 0

    for _ in range(k):
        best_location = 1
        l_scores = [0]*(n+2)
        r_scores = [0]*(n+2)
        last = 0

        for i in range(1, n+1):
            if rooms[i]:
                last = 0
            else:
                l_scores[i] = last
                last+=1

        last = 0

        for i in range(n+1, 1, -1):
            if rooms[i]:
                last = 0
            else:
                r_scores[i] = last
                last+=1

        best_score = 0


        for i in range(1,n+1):
            s = min(l_scores[i], r_scores[i])
            if s > best_score:
                best_score = s
                best_location = i
            elif s == best_score:
                if max(l_scores[i], r_scores[i]) > max(l_scores[best_location], r_scores[best_location]):
                    best_location = i

        rooms[best_location] = True

        min_score = min(l_scores[best_location], r_scores[best_location])
        max_score = max(l_scores[best_location], r_scores[best_location])

        #print(rooms)




    print("Case #{}: {} {}".format(test_num, max_score, min_score))
