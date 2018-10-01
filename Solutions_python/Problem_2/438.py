import sys

input_line = open(sys.argv[1], 'r').read().strip().split('\n')

testcase_no = int(input_line.pop(0))

def parse_testcase(lines):
    trunaround_time = int(lines.pop(0))
    na, nb = lines.pop(0).split()
    asite = dict()
    bsite = dict()
    def fill_siterequest(depature_site, arrival_site, no):
        for x in range(int(no)):
            depature, arrival = lines.pop(0).split()
            depature_time = int(depature[0:2]+depature[3:5])
            arrival_time = int(arrival[0:2]+arrival[3:5])
            if depature_time not in depature_site:
                depature_site[depature_time] = -1
            else:
                depature_site[depature_time] -= 1
            if arrival_time+trunaround_time not in arrival_site:
                arrival_site[arrival_time+trunaround_time] = 1
            else:
                arrival_site[arrival_time+trunaround_time] += 1
    fill_siterequest(asite, bsite, na)
    fill_siterequest(bsite, asite, nb)
    return asite, bsite

out_fp = open(sys.argv[2], 'w')

for cur in range(testcase_no):
    a, b = parse_testcase(input_line)

    def process_train(table):
        keys = table.keys()
        keys.sort()
        cur_train = 0
        req_train = 0
        for key in keys:
            cur_train += table[key]
            if cur_train < 0:
                req_train += (-cur_train)
                cur_train = 0
        return req_train

    na = process_train(a)
    nb = process_train(b)

    print "Case #%i: %i %i"%(cur+1, na, nb)
    out_fp.write("Case #%i: %i %i\n"%(cur+1, na, nb))


