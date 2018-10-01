import sys

num_test_cases = int(sys.stdin.readline())

for test_case in range(num_test_cases):

    (N, M) = [int(i) for i in sys.stdin.readline().split()]

    lawn = [[]]*N
    for row in range(N):
        r = [int(i) for i in sys.stdin.readline().split()]
        lawn[row] = r

    possible = True

    for height in range(1,101):
        done = True
        for row in range(N):
            for col in range(M):
                if height == lawn[row][col]:
                    c = [r[col] for r in lawn]
                    r = lawn[row]
                    if max(c) > height and max(r) > height:
                        possible = False
                        break
                else:
                    done = False
            if not possible:
                break
        if done:
            break
        for row in range(N):
            for col in range(M):
                lawn[row][col] = max(height+1, lawn[row][col])
                    

    print "Case #"+str(test_case+1)+":",
    if possible:
        print "YES"
    else:
        print "NO"
