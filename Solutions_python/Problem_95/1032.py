


def decode(encoded,decoded,table):
    i=0
    while i<len(decoded):
        if encoded[i] != " ":
            table[ord(encoded[i])-97]=decoded[i]
        i=i+1
    return table

def init():
    table=[]
    i=0
    while i<26:
        table.append(' ')
        i=i+1
    return table

def guesstable():
    table = init()
    table = decode("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand",table)
    table = decode("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities",table)
    table = decode("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up",table)
    table[ord("q")-97]="z"
    table[ord("z")-97]="q"
    return table


table = guesstable()
ifile = open("C:\\A-small-attempt0.in","r")
ofile = open("C:\\output.in","w")
n = int(ifile.readline())
i=1
while i<=n:
    sent = ifile.readline()
    ofile.write("Case #"+str(i)+": ")
    for ele in sent:
        if ele == " " or ele=="\n":
            ofile.write(ele)
        else:
            ofile.write(table[ord(ele)-97])
    i=i+1
ifile.close()
ofile.close()


