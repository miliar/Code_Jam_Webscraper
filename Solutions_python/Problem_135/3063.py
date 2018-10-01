n = int(input())
result = ''
for i in range(1, n+1):
    m0 = []
    m1 = []
    m = []
    
    r = int(input()) - 1
    m0 += [list(map(int, input().split()))]
    m0 += [list(map(int, input().split()))]
    m0 += [list(map(int, input().split()))]
    m0 += [list(map(int, input().split()))]
    m0 = m0[r]

    r = int(input()) - 1
    m1 += [list(map(int, input().split()))]
    m1 += [list(map(int, input().split()))]
    m1 += [list(map(int, input().split()))]
    m1 += [list(map(int, input().split()))]
    m1 = m1[r]

    m = [i for i in m0 if i in m1]
    
    if (len(m) == 0):
        result = 'Volunteer cheated!'
    elif (len(m) == 1):
        result = str(m[0])
    else:
        result = 'Bad magician!'

    print ('Case #' + str(i) + ': ' + result)

