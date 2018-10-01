if __name__ == "__main__":
    T = int(raw_input())
    for testcase in xrange(T):
        line = raw_input().split()[1]
        total = 0 #running sum
        friends = 0 #how many friends we have to add
        for i,v in enumerate(line):
            if total < int(i):
                #not enough, add difference as friends
                toadd = i - total
                total = total + toadd
                friends = friends + toadd
            total = total + int(v)
        print "Case #{0}: {1}".format(testcase + 1, friends)


