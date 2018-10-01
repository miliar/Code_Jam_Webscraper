from DomainModel.TestCase import TestCase


class R1A:

    def Solve(self):
        tests = int(input())
        for test in range(tests):
            r,c = list(map(int, input().split()))
            a = []
            cnt=0
            for i in range(r):
                s = input().strip()
                sa = ''
                lc = None
                for c in s:
                    if c!='?':
                        lc=c
                    if lc:
                        sa+=lc
                if sa:
                    sa = sa[0]*(len(s)-len(sa)) + sa
                    a.append((sa,cnt))
                cnt+=1
            print("Case #{}:".format(test+1))
            cnt=0
            for i in range(r):
                print(a[cnt][0])
                if a[cnt][1]==i and cnt+1<len(a):
                    cnt+=1






    def Tests(self):
        yield TestCase("""4
5 2
AB
??
EC
??
??
3 3
G??
?C?
??J
3 4
CODE
????
?JAM
2 2
CA
KE
""","""Case #1:
GGJ
CCJ
CCJ
Case #2:
CODE
COAE
JJAM
Case #3:
CA
KE
        """)

