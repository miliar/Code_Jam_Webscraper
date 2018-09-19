import pdb
import time

def subprocess(f,caseNum,f2):
    print "case num : ",caseNum
    #============== data ================

    ord = []
    ord.append(("O",1))
    ord.append(("B",1))

    #=============== loading ============
    start_loading = time.clock()

    ss = f.readline().split()
    cur = 0
    noA = int(ss[cur])
    cur = cur + 1
    print "noA:",noA
    for i in range(noA):
        r = ss[cur]
        a = int(ss[cur+1])
        cur = cur + 2
        ord.append((r,a))
    print "ord:",ord

    print "loading time : ", time.clock() - start_loading
    #pdb.set_trace()

    #============== process =============
    start_process = time.clock()

    lord = {"O":0,"B":1}
    t = [0,0]
    for i in range(2,len(ord)):
        r = ord[i][0]
        o = ord[i][1]

        wt = abs(o - ord[lord[r]][1])
        st = t[-1] - t[lord[r]]
        add = wt-st
        if add<0:
            add = 0
            
        t.append(t[-1]+add+1)
        lord[r] = i
        
        #print "r:",r
        #print "o:",o
        #print "wt:",wt
        #print "st:",st
        #print "lord:",lord
        #print "t:",t
        #print "add:",add
        #print "===="
        
    print "process time : ", time.clock() - start_process
    #==================

    f2.write("Case #"+str(caseNum+1)+": ")
    f2.write(str(t[-1]))
    f2.write("\n")
    
    return True

def process(inputFile,outputFile):
    print "process ",inputFile
    f = open(inputFile,"r")
    f2 = open(outputFile,"w")
    noCase = int(f.readline())
    print "number of cases : ",noCase
    for c in range(noCase):
        r = subprocess(f,c,f2)
        if not r:
            print "!!!force stop!!!"
            break
    f.close()
    f2.close()

def main():
    path = "D:\\home\\mathieu\\googleJam\\Qualification\\"
    inputFile = path+"A-large.in"
    outputFile = path+"A-large.out"
    process(inputFile,outputFile)
    print "done"

if __name__ == "__main__":
    main()
