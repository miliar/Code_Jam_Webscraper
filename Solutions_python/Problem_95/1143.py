import string
f = open("A-small-attempt0.in")
fwrite = open('A-small-attempt0.out', 'w')
numCases = int(f.readline())
trans = string.maketrans("""a o z q ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv""",
                         """y e q z our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up""")
text = """ejp mysljylc kd kxveddknmc re jsicpdrysi"""
for i in range(0,numCases):
   # print "Case #" + str(i+1) + ": " + f.readline().translate(trans)
    fwrite.write("Case #" + str(i+1) + ": " + f.readline().translate(trans))
f.close()
fwrite.close()
