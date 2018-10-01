import sys, os
from string import rstrip, split

# Open files to read and write
fin = open(os.getcwd() + '\\' + sys.argv[1], 'r')
fout = open(os.getcwd() + '\\' + sys.argv[1] + '.out', 'w')
n = int(rstrip(fin.readline(), '\r\n'))
for case in xrange(n):
    turnover = int(rstrip(fin.readline(), '\r\n'))
    (na, nb) = split(rstrip(fin.readline(), '\r\n'), ' ')
    na = int(na)
    nb = int(nb)
    a_arrives = []
    b_arrives = []
    a_departs = []
    b_departs = []
    for i in xrange(na):
        (depart, arrive) = split(rstrip(fin.readline(), '\r\n'), ' ')
        (hours, minutes) = split(depart, ':')
        departure = int(hours) * 60 + int(minutes)
        (hours, minutes) = split(arrive, ':')
        arrival = int(hours) * 60 + int(minutes)
        a_departs.append(departure)
        b_arrives.append(arrival)
    for i in xrange(nb):
        (depart, arrive) = split(rstrip(fin.readline(), '\r\n'), ' ')
        (hours, minutes) = split(depart, ':')
        departure = int(hours) * 60 + int(minutes)
        (hours, minutes) = split(arrive, ':')
        arrival = int(hours) * 60 + int(minutes)
        b_departs.append(departure)
        a_arrives.append(arrival)
    a_arrives.sort()
    b_arrives.sort()
    a_departs.sort()
    b_departs.sort()
    prev_time = 0
    a_total = 0
    b_total = 0
    a_avail = 0
    b_avail = 0
    while ((len(a_departs) + len(b_departs)) > 0):
        if (len(a_departs) != 0) and ((len(b_departs) == 0) or (a_departs[0] <= b_departs[0])):
            while (len(a_arrives) != 0) and ((a_arrives[0] + turnover) <= a_departs[0]):
                a_arrives = a_arrives[1:]
                a_avail += 1
            if a_avail == 0:
                a_total += 1
            else:
                a_avail -= 1
            a_departs = a_departs[1:]
        else:
            while (len(b_arrives) != 0) and ((b_arrives[0] + turnover) <= b_departs[0]):
                b_arrives = b_arrives[1:]
                b_avail += 1
            if b_avail == 0:
                b_total += 1
            else:
                b_avail -= 1
            b_departs = b_departs[1:]
    fout.write("Case #%d: %d %d\n" % (case + 1, a_total, b_total))
# Close the file streams
fout.close()
fin.close()