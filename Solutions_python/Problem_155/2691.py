
class Recompute(Exception):
    pass


class TestCase(object):
    def __init__(self, index, linput):
        self.index = index
        self.input = linput
        si_max, friends = linput.split(' ', 1)
        self.simax = int(si_max)
        self.friends = [(k, int(v)) for k,v in enumerate(friends[1:], 1)]
        self.newfriends = {}
        self.initially_standing = int(friends[0])
        self.standing_currently = self.initially_standing
#         print "INPUT: ", friends
#         print "Initially standing: {0}".format(self.standing_currently)
        
    def check_will_stand(self, si, members):
        if si in self.newfriends:
            self.standing_currently += self.newfriends[si]
        if self.standing_currently >= si:
#             print "SI: {0}({3}), Standings are: {1}, Additions: {2}".format(si, self.standing_currently, self.newfriends, members)            
            self.standing_currently += members
        else:
            if si in self.newfriends:
                self.newfriends[si] += 1
            else:
                self.newfriends[si] = 1
#             print "=" * 23, self.newfriends
            self.standing_currently = self.initially_standing
            raise Recompute()
        return self.standing_currently
    
    def compute(self):
        for si, members in self.friends:
            self.check_will_stand(si, members)
        
    def get_min_friends(self):
        while True:
            try:
                return self.compute()
            except Recompute:
                continue

class GoogleCodeJamIO(object):
    def __init__(self, input_data='A-large.in'):
        self.fp = open(input_data, 'r')
        self.total_testcases = int(self.fp.readline())
        self.gp = open('output_{0}.txt'.format(input_data), 'wb')
        
    def __del__(self):
        self.fp.close()
        self.gp.close()
        
    def get_testcases(self):
        index = 1
        for message in self.fp:
            if not message.strip("\n"):
                continue
            yield TestCase(index, message.strip("\n"))
            index+=1
        raise StopIteration
    
    def write(self, aud_finder_obj):
        aud_finder_obj.get_min_friends()
        additions = sum(aud_finder_obj.newfriends.values())
        output = "Case #{0}: {1}\n".format(aud_finder_obj.index, additions)
        self.gp.write(output)


if __name__ == '__main__':
    google_case_io = GoogleCodeJamIO()
    for case in google_case_io.get_testcases():
        google_case_io.write(case)
    
    