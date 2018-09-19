def whatpower(l, p, c):
    product = l
    numofpowers = 0
    while product < p:
        product *= c
        numofpowers += 1

    return numofpowers

def smallestpower(num):
    power = 0
    value = 1

    while(num > value):
        value *= 2
        power += 1

    return power


fin = open('B-large.in', 'r')
fout = open('B-large.out', 'w')

for t in range(int(fin.readline())):
    l, p, c = [int(x) for x in fin.readline().strip().split(' ')]

    #find power of c that l needs to multiply to become >= p
    numofpowersneeded = whatpower(l,p,c)

    #find the smallest power of 2 that numofpowersneeded is smaller than
    ans = smallestpower(numofpowersneeded)

    print('Case #', t+1, ': ', ans, sep='', file=fout)
    
fin.close()
fout.close()
