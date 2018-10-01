f = open('A-large.in')
fw = open('A-large.out', 'w')

def to_int_list(c):
    return 1 if c == '+' else 0

def find_zero(s_list, start_index):
    for i in xrange(start_index, len(s_list)):
        if s_list[i] == 0:
            return i
    return -1

T = int(f.readline())
for t in xrange(T):
    S, K = f.readline().split()
    s_list = map(to_int_list, S)
    K = int(K)

    curr = find_zero(s_list, 0)
    count = 0
    possible = True
    while curr >= 0:
        count += 1
        if curr + K > len(s_list):
            possible = False
            break
        for i in xrange(curr, curr + K):
            s_list[i] ^= 1
        curr = find_zero(s_list, curr)

    fw.write('Case #' + str(t + 1) + ': ')
    if possible:
        fw.write(str(count) + '\n')
    else:
        fw.write('IMPOSSIBLE\n')

fw.close()
f.close()
