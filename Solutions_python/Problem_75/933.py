import re

test_cases = []


class TestCase:
    def __init__(self, input_line):
    
        self.c = []
        self.cr = []
        self.o = []
        self.n = ''
          
        self.read(input_line)
        
        #print self.c
        #print self.cr
        #print self.o
        #print self.n
    
    def read(self, input_line):
        input_line = input_line.replace('\n','')
        cls = input_line[0:input_line.index(' ', 0)]
        cl = int(cls)
        position = len(cls)
        
        if cl > 0:
            
            for i in range(cl):
                position = position + 1
                self.c.append(input_line[position:position+2])
                self.cr.append(input_line[position+2:position+3])
                position = position + 3
                
        position = position + 1
        ##print input_line[position:]
        ols = input_line[position:input_line.index(' ', position)]
        ol = int(ols)
        position = position + len(ols)
        
        if ol > 0:
            
            for i in range(ol):
                position = position + 1
                self.o.append(input_line[position:position+2])
                position = position + 2

        
        self.n = input_line[input_line.index(' ', position+1)+1:]
        
        
    def run(self):
        result = self.n
        l = len(result)
        
        i = 1
        for j in range(l):
            #i = i - (len(self.n) - len(result))
            br = result[0:i]
            ir = self.replace(result[0:i])
            result = ir + result[i:]
            i = len(ir) + 1 
            #print 'r', (result, i)
        #result = result.replace(' ', '')
        return '[' + ', '.join(result) + ']'
        
    def replace(self, invoke):
        
        #print 'i', invoke
        
        for i in range(len(self.c)):
            c = self.c[i]
            cr = self.cr[i]
            regex = '('+ c +'|' + c[::-1] +')'
            #print 'cr', regex
            invoke = re.sub(regex, cr, invoke)
            
        for i in range(len(self.o)):
            o = self.o[i]
            regex = '(('+ o[0] +'(.)*'+ o[1] +')|('+ o[1] +'(.)*'+ o[0] +'))'
#            #print 'or', regex
#             if(re.match(regex, invoke)):
#                 invoke = ''
            lc = invoke[-1:]
            oc = o[0]
            if lc == oc:
                oc = o[1]
            #print 'or', o, lc, oc    
            if (lc in o) and invoke.find(oc) > -1:
                invoke = ''
        
        #print 'ir', invoke
        return invoke



def read_input():
    #f = open('ProblemB.in')
    #f = open('B-small-attempt4.in')
    f = open('B-large.in')
    test_case = int(f.readline())
    for i in range(test_case):
        test_cases.append( TestCase(f.readline()) )  
    
    ##print test_cases
    
    
def run_test_cases():
    #f = open('problemB.out', 'w')
    #f = open('B-small-attempt4.out', 'w')
    f = open('B-large.out', 'w')
    for i in range(len(test_cases)):
        test = test_cases[i]
        result = test.run()
        f.write("Case #%d: %s\n" % (i+1, result))
        print "Case #%d: %s" % (i+1, result)
    
def main():
    read_input()
    run_test_cases()

if __name__ == "__main__":
    main()