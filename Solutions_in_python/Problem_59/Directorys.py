import FileUtils
import ThreadingUtils

class dispatch(ThreadingUtils.ThreadDispatcher):
    def runMethod(self,data):
        #print "-- RUNNING --"
        existing,toCreate = data
        #print "Exist ", existing
        #print "Create ",toCreate
        dirLookup = {}
        for x in existing:
            #print "Make: ",x
            parts = x.strip().split("/")
            #print parts
            for idx in range(len(parts)+1):
                newString = "/".join(parts[:idx])
                if newString:
                    dirLookup[newString] = True

        #print dirLookup

        functionCount = 0
        for x in toCreate:
            #print "Make: ",x
            parts = x.strip().split("/")
            #print parts
            for idx in range(len(parts)+1):
                newString = "/".join(parts[:idx])
                if newString:
                    #print idx,newString
                    if dirLookup.get(newString,False):
                        pass
                        #print "Exists"
                    else:
                        #print "Creating"
                        functionCount += 1
                        dirLookup[newString] = True
        #print "OUT:",functionCount
        return functionCount       

class myReader(FileUtils.fileReader):
    def _getNext(self):
        """If more than one line per input Overload to make work"""
        #Get Existing, Create
        
        params = self.reader.next()
        N,M = [int(x) for x in params]
        existing = []
        toCreate = []
        for x in range(N):
            existing.append(self.reader.next()[0])
        for x in range(M):
            toCreate.append(self.reader.next()[0])

        # print "Exist ",existing
        # print "Create ",toCreate
        return (existing,toCreate)

if __name__ == "__main__":
    import time
    stTime = time.time()
    reader = myReader("A-large.in")
    #print reader.next()
    #dispatcher = dispatch(reader)
    #dispatcher.run()
    
    #import sys  
    #sys.exit(0)

#    reader = FileUtils.fileReader()
    #reader = myReader("C-large-practice.in")

    dispatcher = [dispatch(reader) for x in range(1)]
    
    for x in dispatcher:
        x.start()
        
    for x in dispatcher:
        x.join()
        
    reader.writeOut("largeOut.dat")    
    
    edTime = time.time()
    print "Start\t%s "%time.ctime(stTime)
    print "End\t%s "%time.ctime(edTime)
    print "Total\t%s" %(edTime-stTime)


