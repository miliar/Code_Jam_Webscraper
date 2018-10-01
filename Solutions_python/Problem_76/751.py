class Candy:

    def __init__(self, candies):
        self.candies = candies
        self.n = len(candies)



    def max_pile(self):

        def p_add(clist):
            return reduce(lambda x,y: x^y, clist)

        def s_add(clist):
            return reduce(lambda x,y: x+y, clist)

        seans = []

        for m in xrange(1, 2**self.n-1):
            pile0 = []
            pile1 = []

            for nc in range(0, self.n):
                if m&(2**nc):
                    pile1.append(self.candies[nc])
                else:
                    pile0.append(self.candies[nc])

            if p_add(pile0) == p_add(pile1):
                seans.append(max([s_add(pile0), s_add(pile1)]))

        if seans == []:
            return "NO"
        else:
            return max(seans)
            

if __name__ == "__main__":

    out_fmt = "Case #{}: {}\n"

    with open("C-small-attempt0.in", "r") as fin, open("C-small-attempt0.out", "w") as  fout:
        ncases = int(fin.readline())
        for case in range(1, ncases + 1):
            ncandies = int(fin.readline())
            candies = [int(c) for c in fin.readline().strip("\n").split(" ")]

            c = Candy(candies)
            fout.write(out_fmt.format(case, c.max_pile()))
