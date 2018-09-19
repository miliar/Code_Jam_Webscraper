'''
Created on Apr 27, 2012

@author: quilan
'''

#======================================

def parse1(line, inp, aux=[]):
    return parse(line,inp,aux)[0];

def parse(line, inp, aux=[]):
    while len(line)>0 and line[0]==' ': line=line[1:];
    inp = list(inp);
    line = line.split(" ");

    var = [];
    var.extend(aux);
    while len(inp) > 0:
        i=inp[0];
        if(i=="i"):
            var.append(int(line[0]));
            line=line[1:];
            inp=inp[1:];
        elif(i=="f"):
            var.append(float(line[0]));
            line=line[1:];
            inp=inp[1:];
        elif(i=="s"):
            var.append(line[0]);
            line=line[1:];
            inp=inp[1:];
        elif(i=="I"):
            n=int(inp[1]);
            n=var[n];
            var.append(map(int,line[:n]));
            line=line[n:];
            inp=inp[2:];
        elif(i=="F"):
            n=int(inp[1]);
            n=var[n];
            var.append(map(float,line[:n]));
            line=line[n:];
            inp=inp[2:];
        else:
            print "Invalid input: %s"%(inp);
            exit(0);

    return var[len(aux):];

#======================================
