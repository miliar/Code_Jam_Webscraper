'''
Created on 2012-4-9

@author: nvince
'''
def main( filename ):
    
    samples =[]
    samples.append(["ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand"])
    samples.append(["rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities"])
    samples.append(["de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up"])
             
    trans_dict = {}
    for i in xrange(len(samples)):
        sample = samples[i][0]
        sample_out = samples[i][1]
        
        for j in xrange(len(sample)):
            c = sample[j]
            if c not in trans_dict:
                trans_dict[c] = sample_out[j]
    
    
#    for c in "abcdefghijklmnopqrstuvwxyz":
#        out = trans_dict.get(c)
#        if out==None:
#            out = ""
#        print c, out
    trans_dict["q"] = "z"
    trans_dict["z"] = "q"
    
    fin = open(filename)
    fout = open( filename.replace(".in", ".out"), "w")
    caseCount = int(fin.readline())
    
    for caseNum in xrange(1, caseCount+1):
        eachLine = fin.readline().strip()
        line_result = ""
        for c in eachLine:
            line_result += trans_dict[c]
        
        fout.write("Case #%i: %s\n" % (caseNum, line_result))
        
    fin.close()
    fout.close()
    print "%s finished." % (fout.name,)

if __name__ == '__main__':
    main("small.in")
