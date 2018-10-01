from sys import stdin, stdout

def solve():
    n,m = (int(s) for s in stdin.readline().split())
    goal = []
    for row in range(n):
        goal.append(map(int,stdin.readline().split()))
    lawn = []
    #row reduce lawn
    for row in range(n):
        maximum = max(goal[row])
        lawn.append([maximum]*m)

    #column reduce lawn
    for column in range(m):
        maximum = -1
        for row in range(n):
            maximum = max([maximum,goal[row][column]])
        for row in range(n):
            if goal[row][column] is not min([maximum,lawn[row][column]]):
                return "NO"
    return "YES"
    
    

def main():
    testcases = int(stdin.readline())
    for testcase in range(1,testcases+1):
        result = solve()
        fstring = "Case #%d: %s" % (testcase,result)
        print fstring

if __name__ == "__main__":
    main()

