f = open('1.txt', 'r')
T = int(f.readline())

for i in range(T):
    n1 = int(f.readline())
    l1 = [f.readline() for j in range(4)]
    n2 = int(f.readline())
    l2 = [f.readline() for j in range(4)]
    nums1 = map(int, l1[n1-1].split(' '))
    nums2 = map(int, l2[n2-1].split(' '))

    sn = [x in nums2 for x in nums1]
    c = sum(sn)
    if c == 0:
        print "Case #{}: Volunteer cheated!".format(i+1)
    elif c == 1:
        print "Case #{}: {}".format(i+1, nums1[sn.index(True)])
    else:
        print "Case #{}: Bad magician!".format(i+1)

f.close()
