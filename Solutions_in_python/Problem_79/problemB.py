from __future__ import division, print_function

def possible(state, w):
    if len(w) != len(state):
        return False
    for i in xrange(len(state)):
        if (state[i] != "_") and (state[i] != w[i]):
            return False
    return True

def weed_out(state, dic, lis):
    return [w for w in dic if possible(state, w)]

def playable(dic, l):
    for w in dic:
        if l in w:
            return True
    return False

def next_letter(dic, lis):
    for i in xrange(len(lis)):
        l = lis[i]
        if playable(dic, l):
            return (l, lis[i + 1:])

def play_letter(state, word, l):
    ret = ""
    lose = True
    for i in xrange(len(state)):
        if word[i] == l:
            ret += l
            lose = False
        else:
            ret += state[i]
    return (ret, lose)

def eliminate(dic, l):
    return [w for w in dic if l not in w]

def verify_all(dic, state, l):
    ret = []
    for w in dic:
        for i in xrange(len(state)):
            if w[i] == l and state[i] != l:
                break
        else:
            ret.append(w)
    return ret

def score(word, dic, lis, verbose):
    s = 0
    cur_list = lis
    cur_dic = dic
    state = "__________"[0:len(word)]
    while "_" in state:
        if verbose:
            print("%s" % state)
        cur_dic = weed_out(state, cur_dic, cur_list)
        if verbose:
            print("%s" % cur_dic)
        (l, cur_list) = next_letter(cur_dic, cur_list)
        if verbose:
            print("%s => %s" % (l, cur_list))
        (state, lose) = play_letter(state, word, l)
        if lose:
            s += 1
            cur_dic = eliminate(cur_dic, l)
        else:
            cur_dic = verify_all(cur_dic, state, l)
    return s
    
def solve(dic, lis, verbose):
    maxscore = -1
    maxword = ""
    for word in dic:
        sc = score(word, dic, lis, verbose)
        if verbose:
            print("Tried %s with list %s: %d" % (word, lis, sc))
        if (sc > maxscore):
            maxscore = sc
            maxword = word
    if verbose:
        print("%s: %d" % (maxword, maxscore))
    return maxword

def run(input, output, verbose=False):
    T = int(input.readline())
    for index in xrange(1, T + 1):
        [N, M] = [int(x) for x in input.readline().strip().split()]
        D = [input.readline().strip() for x in xrange(N)]
        L = [input.readline().strip() for x in xrange(M)]
        if verbose:
            print("Dict: %s" % D)
            print("Lists: %s" % L)
        words = [solve(D, lis, verbose) for lis in L]
        print("Case #%d: %s" % (index, " ".join(words)), file=output)

