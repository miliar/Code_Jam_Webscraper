
def flip(cur):
        if cur == '+':
                return '-'
        else:
                return '+'

T = int(raw_input())

for tc in range(0, T):
        input = raw_input().split(' ')
        s = input[0]
        k = int(input[1])
        fc = 0
        cur = '+'
        open = []
        close = []
        lens = len(s)
        impossible = False
        for sc in range(0,lens):

                if len(close)>0 and sc == close[0]:
                        cur = flip(cur)
                        close.pop(0)
                        
                if s[sc] != cur:
                        #Impossible
                        if sc > lens - k:
                                impossible = True
                                break
                        #Flip        
                        else:        
                                open.append(sc)
                                close.append(sc+k)
                                fc = fc + 1

                if len(open)>0 and sc == open[0]:
                        cur = flip(cur)
                        open.pop(0)
        if impossible:
                result = 'IMPOSSIBLE'
        else:
                result = str(fc)
        print 'Case #' + str(tc+1) + ': ' + result
