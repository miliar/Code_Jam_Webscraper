from string import maketrans

outtab = """yeqzour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up"""
intab =  """aozqejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"""
trantab = maketrans(intab, outtab)

in_file = open("qualA.small")

in_file.readline()

ind = 1
for line in in_file:
    if (line[-1] == "\n"):
        line = line[:-1]
    print "Case #%d: %s" % (ind, line.translate(trantab))
    ind += 1
    
    