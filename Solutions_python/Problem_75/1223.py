'''
Created on May 6, 2011

@author: jonathanbona
'''

'''
Created on May 6, 2011

@author: jonathanbona
'''
combos = {}
opps = {}

def parseInput(fname):
    f = open(fname,'r');
    of = open(fname+'out','w')
    
    num = int(f.readline().strip());
    
    print "Processing ",num," cases"
    
    # for each case
    for i in range(1,num+1):
        case = handlecase(f.readline().strip());
        #print case
        of.write("Case #"+str(i)+": "+case+"\n");


def handlecase(line):
    global combos
    global opps
    combos = {}
    opps = {}
    elts = line.split();
    elts.reverse();

    C = int(elts.pop());

    # get the combinations
    for _ in range(C):
        combo = elts.pop()
        combos[combo[0]] = {combo[1] : combo[2]} 
        combos[combo[1]] = {combo[0] : combo[2]} 

    D = int(elts.pop())

    # get the oppositions
    for _ in range(D):
        combo = elts.pop();
        opps[combo[0]] = combo[1]
        opps[combo[1]] = combo[0] 

    # get N, the number of characters
    N = int(elts.pop())

    return invoke(elts.pop(),N)

def opponentp(worklist, elt):
    opp = opps.get(elt)
    for e in worklist:
        if e == opp:
            return True
    return False

def replacement(elt1, elt2):
    combo = combos.get(elt1)
    if combo != None:
        return combo.get(elt2)
        

def invoke(baseElts, N):
    #print "invoking on ", N, " baseElts: ", baseElts
    working = []

    for elt in baseElts:
        if len(working) > 0: # no combos or oppositions if this is the first elt
            lastelt = peek(working)
            repl = replacement(lastelt, elt)
            
            if repl != None:
                working.pop()
                working.append(repl)
            else:
                if opponentp(working, elt):
                    working = []
                else: # no combo, no opponent: just put it on the list
                    working.append(elt)
        else: # if the working list was empty, just put this element on it
            working.append(elt)
         
    return printableCase(working)

def printableCase(case):
    result = "["
    if len(case) > 0:
        for e in range(len(case)-1):
            result=result+case[e]+", "
        result=result+case[len(case)-1]
    result=result+"]"
    return result



def peek(list):
    return list[len(list)-1]
        
if __name__ == '__main__':

    parseInput('B-small-attempt0.in')
    pass