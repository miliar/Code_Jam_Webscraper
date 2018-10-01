'''
Created on May 6, 2011

@author: mk
'''


def solve(fin, fout):
    cases = int(fin.readline())
    for index in range(cases):
        _ignore = fin.readline()
        candies = map(int, fin.readline().strip().split())
        fout.write(solveCase(index+1, candies))


def solveCase(index, candies):
    total_value = reduce(lambda x, y: x ^ y, candies, 0)
    if total_value:
        return "Case #{0}: NO\n".format(index)
    else:
        cheapest_candy = min(candies)
        return "Case #{0}: {1}\n".format(index, sum(candies) - cheapest_candy)


def testSolve():
    from StringIO import StringIO
    input = StringIO("""2
5
1 2 3 4 5
3
3 5 6""")
    solve(input, sys.stdout)

if __name__ == '__main__':
    import sys
    #testSolve()
    solve(sys.stdin, sys.stdout)
