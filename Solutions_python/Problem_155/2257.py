import sys

lines = [line.strip() for line in sys.stdin]

cases = int(lines[0])

for i, case in enumerate(lines[1:]):
    smax, audience = case.split()
    smax = int(smax)
    invited = 0
    standing = 0
    for j, num in enumerate(audience):
        num = int(num)
        if standing >= j:
            standing += num
        elif num > 0:
            invite = j - standing
            invited += invite
            standing += num + invite

    print "Case #" + str(i + 1) + ": " + str(invited)
