

class CandyGame(object):
    def __init__(self, candyStr):
        self.candies = sorted([int(x) for x in candyStr.split()])
        self.candies.reverse()
        self.maxPatSum = 2**(len(bin(self.candies[0]))-2)
        self.maxWin = 0
        self.maxIdx = len(self.candies)
        self.maxCandieSum = []
        for i in range(len(self.candies)):
            self.maxCandieSum.append(sum(self.candies[i:]))

    def variants(self, seanXor=0, seanSum=0, patXor=0, patSum=0, idx=0):
        if idx==self.maxIdx:
            #test, if patrick's sum are equal
            #print "seanXor:%d, seanSum:%d, patXor:%d, patSum:%d" % (seanXor, seanSum, patXor, patSum)
            if seanSum>0 and patSum > 0 and seanXor == patXor:
                self.maxWin = max(self.maxWin, seanSum)
                #print self.maxWin
        else:
            ##if the sum of sean greater the possible Xor sum
            #if seanXor>self.maxPatSum:
            #    return

            #if the left candies sum lower than reach maxSum
            if seanSum + self.maxCandieSum[idx]<self.maxWin:
                return

            #give sean the next candy
            self.variants(seanXor ^ self.candies[idx], 
                          seanSum + self.candies[idx], 
                          patXor, patSum, idx+1)
            #give sean the next candy
            self.variants(seanXor, seanSum,
                          patXor ^ self.candies[idx], 
                          patSum + self.candies[idx], idx+1)

if __name__ == "__main__":
    import sys
    for case in range(int(sys.stdin.readline())):
        sys.stdin.readline()
        game = CandyGame(sys.stdin.readline())
        game.variants()
        if game.maxWin:
            print "Case #%d: %d" % (case+1, game.maxWin)
        else:
            print "Case #%d: NO" % (case+1)
