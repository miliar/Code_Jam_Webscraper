from random import *

f = open("gorosort.small.in", "r")

T = int(f.readline())

N = []
A = []
S = []

for t in range(0, T):
    n = int(f.readline())
    N.append(n)

    A.append([])
    v = f.readline().split(" ")
    for i in range(0, n):
        A[t].append(int(v[i]))

f.close()

def binary_search(integers, t0, i0, j0):
    mid = ((j0 - i0) / 2) + i0
    t_mid = integers[mid]

    if t_mid == t0:
        return mid
    elif j0 <= i0:
        return -1
    elif t_mid > t0:
        return binary_search(integers, t0, i0, mid - 1)
    elif t_mid < t0:
        return binary_search(integers, t0, mid + 1, j0)


def stupid_find(S, k):
    result = []
    for i in range(0, len(S)):
        if S[i] == k:
            result.append(i)
    return result


def find_path_to(index, n, A, S, i, path):
    k = A[i]
    nextsteps = stupid_find(S, k)

    if (n == 1):
        if index in nextsteps:
            return path + [index]
        else:
            return []
    else:
        for j in nextsteps:
            p = find_path_to(index, n-1, A, S, j, path + [j])
            if len(p) > 0:
                return p
        return []
            
        
    
def find_n_cycle(n, A, S):
    for i in range(0, len(A)):
        if (n == 1):
            if A[i] == S[i]:
                return [i]
        else:
            cycle = find_path_to(i, n, A, S, i, [])
            if len(cycle) > 0:
                return cycle
    return []


def get_e(A):

    S = sorted(A)

    depth = 1
    expected = 0
    
    while (True):
        cycle = find_n_cycle(depth, A, S)

        if len(cycle) == 0:
            depth += 1
        elif len(cycle) > 2:
            shuffle(cycle)
            L = cycle[:]

            expected += 1 + get_e(L)

            cycle = sorted(cycle)
            for i in range(len(cycle)-1, -1, -1):
                del A[cycle[i]]
                del S[cycle[i]]
        else:
            cycle = sorted(cycle)

            expected += 2*(depth-1) # slag för att fixa en cykel
            
            for i in range(len(cycle)-1, -1, -1):
                # remove cycle
                del A[cycle[i]]
                del S[cycle[i]]

        if len(A) == 0:
            return expected

def half_trim(n):
    low = int(n)
    if (n < low + 0.25):
        return low
    elif (n > low + 0.75):
        return low + 1
    else:
        return low + 0.5
                
f = open("gorosort.out", "w")

for t in range(0, T):

    P = A[t][:]

    E = []
    for i in range(0, 1000):
        E.append(get_e(P[:]))

    expected = sum(E) / float(len(E))

    expected = half_trim(expected)

    f.write("Case #" + str(t + 1) + ": " + str(expected) + "\n")

f.close()
        
print "done"
















        
        
