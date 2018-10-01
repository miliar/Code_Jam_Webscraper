class Bathroom(object):
    def __init__(self, num_bathrooms):
        self.num_bathrooms = num_bathrooms
        self.bathrooms = [False] * num_bathrooms
        self.left_dist = [0] * num_bathrooms
        self.right_dist = [0] * num_bathrooms
        self.min_dist = [0] * num_bathrooms
        self.max_dist = [0] * num_bathrooms

        [self.computeDist(i) for i in xrange(num_bathrooms)]

    def computeDist(self, i):
        left, right = self.bathroomDistances(i)
        self.left_dist[i] = left
        self.right_dist[i] = right
        self.min_dist[i] = min(left, right)
        self.max_dist[i] = max(left, right)

    def bathroomDistances(self, i, return_indexes=False):
        li = i - 1
        ri = i + 1

        while li >= 0 and self.bathrooms[li] == False:
            li -= 1

        while ri < self.num_bathrooms and self.bathrooms[ri] == False:
            ri += 1

        left = i - li - 1
        right = ri - i - 1

        if return_indexes:
            return li, ri

        return left, right
        
    def assignBathroom(self):
        options = [(self.min_dist[ind], self.max_dist[ind], ind) \
                for ind in xrange(self.num_bathrooms) \
                if not self.bathrooms[ind]]

        sorted_options = sorted(options, key= lambda x: (-min(x[0], x[1]), -max(x[0], x[1]), x[2]))

        req_option = sorted_options[0]

        #mark as occupied
        self.bathrooms[req_option[2]] = True

        #find left and right occupied indexes and recompute in between bathroom distances
        li, ri = self.bathroomDistances(req_option[2], return_indexes=True)
        for t in xrange(li+1, req_option[2]):
            self.computeDist(t) 

        for t in xrange(req_option[2]+1, ri):
            self.computeDist(t) 

        return min(req_option[0], req_option[1]), max(req_option[0], req_option[1])

    def assignAllPeople(self, num_people):
        ls = rs = 0
        for i in xrange(num_people):
            ls, rs = self.assignBathroom()

        return ls, rs

input_size = input()

for i in xrange(input_size):
    inp = raw_input()
    num_bath, num_people = inp.split(" ")
    num_bath = int(num_bath)
    num_people = int(num_people)

    b = Bathroom(num_bath)
    mini, maxi = b.assignAllPeople(num_people)

    print "Case #%d:"%(i+1), maxi, mini
