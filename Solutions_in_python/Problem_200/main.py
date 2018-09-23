fr = open('B-small-attempt0.in', 'r')
fw = open('B-small-attempt0.out', 'w')
test_cases = int(fr.readline())

for i in range(test_cases):
    tidy = False
    list1 = []
    n = int(fr.readline().rstrip('\n'))
    for j in reversed(range(n+1)):
        s = len(str(j))
        t = j
        for k in range(s):
            c = t%10
            list1.append(c)
            t=int(t/10)
        list1.reverse()
        if sorted(list1) == list1:
            fw.write("Case #" + str(i+1) + ": " + str(j)+"\n")
            list1.clear()
            break;
        list1.clear()

