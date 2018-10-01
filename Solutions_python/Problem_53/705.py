import sys

def do_case(count=0, snaps=0):
    mod_num = 2**count
    if snaps % mod_num == mod_num - 1:
        return 'ON'
    return 'OFF'

try:
    filename = sys.argv[1]
except IndexError:
    print("Enter a valid input file.")
    exit()
cases = []
f_in = open(filename)
fname_parts = filename.split('.')
fname_parts[1] = 'out'
fname_out = '.'.join(fname_parts)
f_out = open(fname_out, 'w')
f_in.readline() # skip
count = 1
for test_case in f_in:
    parts = test_case.split()
    tc_count = int(parts[0])
    tc_snaps = int(parts[1])
    f_out.write(
        "Case #%s: %s\n" % (
            count,
            do_case(
                count=tc_count,
                snaps=tc_snaps)))
    count += 1
f_in.close()
f_out.close()
