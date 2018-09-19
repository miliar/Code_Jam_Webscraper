
class TestCase(object):
    def __init__(self, input_):
        self.smax, self.ns = input_.split()
        self.ns = map(int, self.ns)
        self.smax = int(self.smax)
        self.people_up = 0
        self.friends_in = 0

    def solve(self):        
        for shy_level in xrange(self.smax):
            self.people_up += self.ns[shy_level]
            if self.people_up < shy_level + 1:
                self.friends_in += 1
                self.people_up += 1
        return self.friends_in
            

def main():
    ntest = int(raw_input())
    for itest in range(ntest):
        print "Case #{}: {}".format(itest + 1, TestCase(raw_input()).solve())

if __name__ == "__main__":
    main()
