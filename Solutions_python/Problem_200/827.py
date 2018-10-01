
def ok(s):
    if len(s) == 1:
        return True
    if s[0] > s[1]:
        return False
    if s[0] < s[1]:
        return True
    return ok(s[1:])

num_cases = int(raw_input())
for case in range(num_cases):
    s = raw_input()
    ans = ''
    sosad = False
    for i in range(len(s)):
        if sosad:
            ans += '9'
        else:
            if ok(s[i:]):
                ans += s[i]
            else:
                sosad = True
                if s[i] != '1':
                    ans += chr(ord(s[i])-1)

    print 'Case #%d: %s' % (case+1,ans)

