
debug = False

def dep(msg):
    if debug:
        print msg

def preprocess(input_data1, input_data2):
    result = {}
    rests = input_data2.split(" ")
    result['N'] = int(input_data1)
    result['m'] = [int(i) for i in rests]
    #dep(result)
    return result

def algo(pd):
    result = 0

    N = pd['N']
    m = pd['m']

    result1 = 0
    for i in range(0,N-1):
        if m[i+1] < m[i]:
            result1 += m[i] - m[i+1] 

    result2 = 0
    max_eat = 0
    for i in range(0,N-1):
        if (m[i] > m[i+1])and (m[i] - m[i+1] > max_eat):
            max_eat = m[i] - m[i+1]

    for i in range(0,N-1):
        r = m[i] - max_eat
        if r <= 0:
            result2 += m[i]
        else:
            result2 += max_eat

    dep( str(result1) + "," + str(result2))

    return [result1, result2]

def answer(ro, i):
    result = "Case #%d: %d %d" %(i+1, ro[0], ro[1])
    dep("result: " + result)
    return result

"""main"""

N = int(raw_input())
dep("N: %d" %N)

result = []
out = ''

for i in range(0, N):
    result.append( answer( algo( preprocess(raw_input(), raw_input()) ), i) )

dep("=================")
out = '\n'.join(result)
print out

