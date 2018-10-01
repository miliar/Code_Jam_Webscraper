import re

l, d, n = raw_input().split(' ')
words = []
for x in range(int(d)):
    word = raw_input()
    words.append(word)

tests = []
for y in range(int(n)):
    test = raw_input()
    tests.append(test)

    t = ''
    if len(re.findall(r'\(.*?\)', test)) > 0:
        test_a = re.sub(r'\(', '[', test)
        test_b = re.sub(r'\)', ']', test_a)
        t = test_b
    else:
        t = test

    #print 'test:', t
    found = 0
    for word in words:
        if len(re.findall(t, word)) > 0:
            found += 1
            #print word, 'ok'

    print "Case #%d: %d" % (y+1, found)


