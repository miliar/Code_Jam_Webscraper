#The kth group starts clapping if sum(i=0 to k-1 of people[i]) > k

# shy=0 group starts clapping
# shy=1 group starts clapping if people[0] > 1
# shy=2 group starts clapping if people[0]+people[1] > 2

# example:
#012345
#110011
# s0 starts clapping, total = 1
# s1 starts clapping, total = 2
# s2 no people
# s3 no people
# s4 not clapping, because total = 2. Need to add two people at k=total=2. So now s4 clapping, total=5

def case(audience):
    total = 0
    to_add = 0
    for shyness, people in enumerate(audience):
        missing = max(0, shyness - total)
        to_add += missing
        total += people + missing

    return to_add

t = int(raw_input())
i = 0
while i < t:
    i += 1
    _, audience = raw_input().split()
    audience = [int(c) for c in audience]

    print "Case #%d: %d" % (i, case(audience))
