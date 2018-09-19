#lawnmower problem

def lm(filepath):
    f = open(filepath)
    cases = int(f.readline())
    for i in range(cases):
        l = f.readline()
        l = l.split()
        n = int(l[0])
        m = int(l[1])
        lawn = []
        for k in range(n):
            nextrow = f.readline()
            nextrow = nextrow.split()
            lawn.append(nextrow)
        print("Case #" + str(i+1) + ": " + solve(lawn))

def solve(lawn):
    #can't be the smallest on the row and the smallest on the column it's just not possible
    #basically it can't be boxed in by bigger things
    for i in range(len(lawn)):
        for k in range(len(lawn[i])):
            #now looking at lawn[i][k]
            val = lawn[i][k]
            left_bound = False
            right_bound = False
            up_bound= False
            low_bound = False
            for rowele in range(len(lawn)):
                if rowele < i and lawn[rowele][k] > lawn[i][k]:
                    left_bound = True
                if rowele > i and lawn[rowele][k] > lawn[i][k]:
                    right_bound = True
            for colele in range(len(lawn[0])):
                if colele < k and lawn[i][colele] > lawn[i][k]:
                    up_bound = True
                if colele > k and lawn[i][colele] > lawn[i][k]:
                    low_bound = True
            if (left_bound or right_bound) and (up_bound or low_bound):
                return 'NO'
    return 'YES'
