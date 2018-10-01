import sys


def find_doubles(num1, num2):
    found = {}
    all_range = range(num1, num2 + 1)
    for i in all_range:
        snum = str(i)
        for de in range(1, len(snum)):
            new_snum = snum[de:] + snum[:de]
            if new_snum[0] == '0':
                continue
            new_num = int(new_snum)
            if new_num == i or new_num not in all_range:
                continue
            
            found[(min(i, new_num), max(i, new_num))] = ''
    return len(found.keys())
        

def calc_doubles(intxt):
    lines = intxt.split('\n')
    lines_total = int(lines[0])
    outtxt = ''
    for line_num in range(1, lines_total + 1):
        outtxt += "Case #%s: %s\n" % (line_num, find_doubles(*map(int, lines[line_num].split(' '))))
    return outtxt[:-1]

if __name__ == '__main__':
    infile = sys.argv[1]
    outfile = sys.argv[2]
    with open(infile, 'r') as _ifile:
        with open(outfile, 'wb') as _ofile:
            _ofile.write(calc_doubles(_ifile.read()))
