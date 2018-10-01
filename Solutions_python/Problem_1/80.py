import sys

class NoImplode:

    def __init__(self, engines, queries):
        self.engines = list(engines)
        self.permit = list(engines)
        self.count_switch = 0
        self.queries = list(queries)
        self.rev_queries = list(queries)
        self.rev_queries.reverse()
        
    def change_engine(self, current_engine):
        self.permit = list(self.engines)
        self.permit.remove(current_engine)
        self.count_switch += 1

    def process_queries(self):
        for item in self.rev_queries:
            if item in self.permit:
                self.permit.remove(item)
                #print "processing " + item + ", permitted: "+ repr(self.permit)
                if not self.permit:
                    self.change_engine(item)
                    #print "switch, permitted: " + repr(self.permit)
        return self.count_switch

def processFile(source, target):
    sf = open(source)
    tf = open(target,"w")
    num_cases = int(sf.readline())
    for case in range(1,num_cases+1):
        e=[]
        q=[]
        num_engines = int(sf.readline())
        for i in range(0,num_engines):
            e.append(sf.readline().strip('\n'))
        num_queries = int(sf.readline())
        for i in range(0,num_queries):
            q.append(sf.readline().strip('\n'))
        no_implode = NoImplode(e,q)
        case_result = no_implode.process_queries()
        newline = 'Case #' + repr(case) + ': ' + repr(case_result)
        #print(newline)
        tf.write(newline)
        if not case==num_cases: tf.write('\n')

    sf.close
    tf.close


def main(argv = None):
    if argv is None:
        argv = sys.argv
    if (len(argv)>2):
        processFile(argv[1], argv[2])
    #source = 'A-small.in'
    #target = 'A-small.out'
    
if __name__ == "__main__":
    main()
    