ntests = int(input())

def readcase():
    n = int(input())
    return set(int(i) for i in [input() for _ in range(4)][n-1].split())

for i in range(ntests):
    res = readcase().intersection(readcase()) 
    if not res:
        t = 'Volunteer cheated!'
    elif len(res) > 1:
        t = 'Bad magician!'
    else:
        t = str(res.pop())
    print('Case #{}: {}'.format(i+1, t))        