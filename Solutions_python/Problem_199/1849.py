

def flip(s, pos, k):
    lst = list(s)
    for i in range(pos, pos+k):
        if lst[i] == '-':
            lst[i] = '+'
        else:
            lst[i] = '-'
    return ''.join(lst)



t = int( input() )

for numcase in range(1, t+1):

    s, k = input().split()
    k = int(k)

    s_length = len(s)

    count = 0

    for i in range(s_length-k+1):

        if s[i] == '-':
            s = flip(s, i, k)
            count += 1

    if '-' in s:
        print('Case #{}: IMPOSSIBLE'.format(numcase))
    else:
        print('Case #{}: {}'.format(numcase, count))
