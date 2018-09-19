import threading
import random
import FileUtils #For Testing
import time

class ThreadDispatcher(threading.Thread):
    """Nice Simple Class to Setup and Run Tasks"""
    def __init__(self,fileHandler):
        """
        Create A dispatcher
        @param fileHandler: Link to object that serves data
        """
        threading.Thread.__init__(self)
        self.fileHandler = fileHandler
        

    def run(self):
        """Generallised Running"""
        while True:
        #for x in range(10):
            case,data = self.fileHandler.next()
#            print case
            if not case:
                break
            else:
                output = self.runMethod(data)
            self.fileHandler.appendOut(case,output)

    def runMethod(self,data):
        """Overload this"""
        
        #time.sleep(float(data[0]))
        #print data
        return data
            
if __name__ == "__main__":
    """TOTAL = 26.72"""

    """One Thread 26.77092
    Two 13.458
    5 = 5.548
    """
    # with open("testInput.dat","w") as fd:
    #     fd.write("100\n")
    #     sumV = 0.0
    #     for x in range(100):
    #         val = random.random()/2.0
    #         sumV += val
    #         fd.write("%s\n" %val)
    # print sumV
    stTime = time.time()

    handler = FileUtils.fileReader("testInput.dat")
    dispatch = [ThreadDispatcher(handler) for x in range(5)]

    for x in dispatch:
        x.start()
        
    for x in dispatch:
        x.join()
        
    handler.writeOut("TestOutput.dat")
    edTime = time.time()

    print "Start time %s "%time.ctime(stTime)
    print "End time %s "%time.ctime(edTime)
    print "Total Time %s" %(edTime-stTime)
    # while True:
    #     case,data = handler.nextCaseCatch()
    #     print "%s %s" %(case,data)
    #     if not case:
    #         break
                
            
