
res_str = 'Case #{0}: {1}'

test_cases = int(input())

def flip(s):
    flipped_str = ''
    for c in s:
        if c == '-':
            flipped_str += '+'
        else:
            flipped_str += '-'
    return flipped_str
            
for t in range(1, test_cases+1):
    p, k = input().split()
    k = int(k)
    res = 0
    for i in range(len(p)):
        if p[i] == '-':
            if len(p)-i >= k:
                p = p[0:i] + flip(p[i:i+k]) + p[i+k:]
                res += 1
            else:
                break
    if p.find('-') == -1:
        print(res_str.format(t, str(res)))
    else:
        print(res_str.format(t, 'IMPOSSIBLE'))
