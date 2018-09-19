def magicResult(fs, ss, fr, sr):
    res = list(set(fs[fr-1]).intersection(set(ss[sr-1])))
    if len(res) > 1:
        return "Bad magician!"
    elif len(res) == 0:
        return "Volunteer cheated!"
    else:
        return res[0]

def formSet():
    output = []
    for i in xrange(4):
        temp_list = []
        data = fp.readline().strip()
        for each_char in data.split():
            temp_list.append(int(each_char))
        output.append(temp_list)
    return output
            
with open('A-small-attempt1.in', 'r') as fp:
    for tc in xrange(int(fp.readline())):
        first_row = int(fp.readline())
        first_set = formSet()
        sec_row = int(fp.readline())
        sec_set = formSet()
        print "Case #%d: %s" % (tc+1, magicResult(first_set, sec_set, first_row, sec_row))
