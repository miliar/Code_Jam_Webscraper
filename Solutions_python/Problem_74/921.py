
test_cases = []


class TestCase:
    def __init__(self, input_line):
    
        self.all_q = []
        self.robo_q = {'O':[],'B':[]}
        
        
        self.steps = 0
        self.current_position = 0
        self.who_in_wait = 0
        
        self.b_key = 1
        self.o_key = 1
        self.current_position = 1
        
        self.o_ct = 0
        self.b_ct = 0
        
        self.read(input_line)
    
    
    def read(self, input_line):
        input_line = input_line.split();
        i = 1
        position = 0
        lines = int(input_line[0])
        while(position < lines):
            (robo, key) = (input_line[i],int(input_line[i+1]))
            self.all_q.append((robo, key))
            self.robo_q[robo].append( (position,key) )
            
            i = i + 2
            position = position +1
        
        #print self.all_q
        #print self.robo_q
        
        
        
    def run(self):
        #print "running a test case"
        o_push = False
        p_push = False
        
        while(self.current_position <= len(self.all_q)):
            (robo, key) = self.all_q[self.current_position-1]
            (o_p, o_k) = (0,0)
            (b_p, b_k) = (0,0)
            
            if(len(self.robo_q['O']) > self.o_ct):
                (o_p, o_k) = self.robo_q['O'][self.o_ct]
                
            if(len(self.robo_q['B']) > self.b_ct):
                (b_p, b_k) = self.robo_q['B'][self.b_ct]
            
            
            if((o_p, o_k) == (0,0) and (b_p, b_k) == (0,0)):
                break;
            
            o_push = o_k == self.o_key
            p_push = b_k == self.b_key
            
            if(o_k > self.o_key):
                self.o_key = self.o_key + 1
            elif(o_k < self.o_key):
                self.o_key = self.o_key - 1

            if(b_k > self.b_key):
                self.b_key = self.b_key + 1
            elif(b_k < self.b_key):
                self.b_key = self.b_key - 1
            
            self.steps = self.steps + 1
            #print self.steps, self.o_key, self.b_key, (o_push, p_push, self.current_position, self.o_ct, self.b_ct, o_k, b_k)    
                
            if(robo == "O" and o_k == self.o_key):
                if o_push:
                    self.o_ct = self.o_ct + 1
                    self.current_position = self.current_position + 1
                    o_push = False
                    
                    if b_k == self.b_key:
                        p_push = True
                else:
                    o_push = True
                #self.steps = self.steps + 1
            if(robo == "B" and b_k == self.b_key):
                if p_push:
                    self.b_ct = self.b_ct + 1
                    self.current_position = self.current_position + 1
                    p_push = False
                    
                    if o_k == self.o_key:
                        o_push = True
                else:
                    p_push = True
            
        return self.steps    

def read_input():
    #f = open('problemA.in')
    f = open('A-large.in')
    test_case = int(f.readline())
    for i in range(test_case):
        test_cases.append( TestCase(f.readline()) )  
    
    #print test_cases
    
    
def run_test_cases():
    f = open('A-large.out', 'w')
    for i in range(len(test_cases)):
        test = test_cases[i]
        seconds = test.run()
        f.write("Case #%d: %d\n" % (i+1, seconds))
        print "Case #%d: %d" % (i+1, seconds)
    
def main():
    read_input()
    run_test_cases()

if __name__ == "__main__":
    main()