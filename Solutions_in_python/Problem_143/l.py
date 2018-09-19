import cPickle as pickle

# dic = {}
# for i in range(1001):
#    for j in range(1001):
#        dic[(i, j)] = i & j
# pickle.dump(dic, open('t.pkl', 'w'), protocol=-1)

dic = pickle.load(open('t.pkl'))

T = int(raw_input())
for i in range(T):
    A, B, K = map(int, raw_input().split())
    # print A, B, K
    count = 0
    for p in range(A):
        for q in range(B):
            if dic[(p, q)] < K:
                count += 1

    print "Case #%s: %s" % ((i + 1), count)