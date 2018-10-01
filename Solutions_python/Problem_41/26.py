
def getnext(s):
    lst = list(reversed('0'+s))
    for i in range(1, len(lst)):
        if lst[i] < max(lst[:i]):
            v = min([x for x in lst[:i] if x > lst[i]])
            lst[lst.index(v)] = lst[i]
            lst[i] = v
            break
    lst[:i] = sorted(lst[:i], reverse=True)
    return ''.join(reversed(lst)).lstrip('0')

ncase = int(raw_input())
for i in range(ncase):
    num = raw_input()
    ans = getnext(num)
    print 'Case #%d: %s' % (i+1, ans)
