def allhappy(lstS):
    for s in lstS:
        if s == '-':
            return False
    return True

def flip(lstS, sp, n):
    for i in xrange(sp,sp+n):
        if lstS[i] == '+':
            lstS[i] = '-'
        else:
            lstS[i] = '+'
    return lstS

def fliptimes(state, k):
    state = [ch for ch in state]
    N = len(state)
    position = 0
    times = 0

    while position < N:
        # print state
        if allhappy(state):
            return times
        if state[position] == '-':
            p = min(N - k, position)
            state = flip(state, p, k)
            times +=1
        position += 1
    if allhappy(state):
        return times
    return 'IMPOSSIBLE'


if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(1, t + 1):
      state, flipper = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
      flipper = int(flipper)
      print "Case #{}: {}".format(i, fliptimes(state, flipper))
