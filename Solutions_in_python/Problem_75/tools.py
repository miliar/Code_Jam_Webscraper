def read_file(file):
    file = open(file)
    lines = file.readlines()
    file.close()
    for i in xrange(0, len(lines)):
        lines[i] = lines[i].strip()
    return lines

def insert_case(lst):
    """ insert caseN# in each line of list """
    for i in xrange(0, len(lst)):
        lst[i] = "Case #%d: " % (i+1) + lst[i]
    return lst

def write_file(lst, file):
    """ write list to file as lines """
    lines = lst
    for i in xrange(0, len(lines)):
        lines[i] += "\n"
    file = open(file, "w")
    file.writelines(lines)
    file.close()
