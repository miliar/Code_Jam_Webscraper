class Solution():

    '''
    ---+----++-

    '''

    def tn(self, n):
        s, index= str(n), -1
        dic = {s[0]: 0}
        for i, c in enumerate(s[1:], 1):
            if c < s[i-1]:
                index = i-1 if s[i-1] not in dic else dic[s[i-1]]
                break
            elif c == s[i-1]:
                continue
            else:
                dic[c] = i if c not in dic else dic[c]
        return int(s[:index] + str(int(s[index])-1) + '9'*(len(s)-index-1)) if index!=-1 else n

o = Solution()
n = int(raw_input())
f = open('output2', 'wr')
for i in xrange(n):
    num = int(raw_input())
    f.write('Case #%d: %d\n' % (i+1, o.tn(num))) 



