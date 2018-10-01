import sys

filename = sys.argv[1]
curfile = file(filename, 'rb')

audiences = []
testcases = curfile.readlines()[1:]
for testcase in testcases:
    max_shyness = testcase.split(' ')[0]
    audience = []
    for char in testcase.split(' ')[1].strip():
        audience.append(int(char))
    audiences.append(audience)
    
audiencecount = 1
for audience in audiences:
    minfriends = 0
    total = 0
    shyness = 0
    while shyness < len(audience):
        members = audience[shyness]
        if total < shyness:
            minfriends = max(minfriends, shyness - total)
        total += members
        shyness += 1

    print "Case #%d: %d" % (audiencecount, minfriends)
    audiencecount += 1
        
