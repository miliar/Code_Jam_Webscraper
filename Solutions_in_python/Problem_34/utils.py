ex=execfile
readpath="C:\\Users\\danra\\Downloads\\"
writepath="C:\\Users\\danra\\Downloads\\"

def read1(fn,mode='r'):
    return [x[:-1] for x in file("%s%s" % (readpath,fn),mode).readlines()]

def write1(fn,lines,mode='w'):
    file("%s%s" % (writepath,fn),mode).writelines([x+'\n' for x in lines])

def intersect(sets):
    if len(sets)==0:
        return set()
    res = set(sets[0])
    for x in sets[1:]:
        res.intersection_update(x)
    return res

