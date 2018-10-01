#!/usr/bin/python

def PI(array):
    res = 1
    for elem in array:
        res *= elem
    return res

'''Core Training - 2017 1C'''
def small_solver(N, Ps, U):
    sorted_Ps = sorted(Ps)
    #print len(Ps), U, sum(Ps)
    #print sum(sorted_Ps) + U
    for idx, p in list(enumerate(sorted_Ps))[:-1]:
        if U > (idx+1) * (sorted_Ps[idx+1] - sorted_Ps[idx]):
            U -= (idx+1) * (sorted_Ps[idx+1] - sorted_Ps[idx])
            for j in xrange(idx+1):
                sorted_Ps[j] = sorted_Ps[idx+1]
        else:
            for j in xrange(idx+1):
                sorted_Ps[j] += U/(idx+1)
            U = 0
            break
    for j in xrange(len(sorted_Ps)):
        sorted_Ps[j] += U/len(sorted_Ps)
    #print sorted_Ps
    return PI(sorted_Ps)

def main():
    t_val = input('')
    for c_idx in xrange(t_val):
        N, K = map(int, raw_input('').split())
        U = float(raw_input(''))
        Ps = map(float, raw_input('').split())
        print 'Case #%d: %f' % (c_idx + 1, small_solver(N, Ps, U))

main()