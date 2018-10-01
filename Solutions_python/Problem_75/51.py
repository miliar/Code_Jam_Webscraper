import sys

outf = []
def pout(text):
    outf.append("Case #" + str(pout.case) + ": " + text + "\n")
    pout.case += 1
pout.case = 1

def get_input(infname):
    with open(infname, "r") as f:
        return map(lambda a: a.strip(), f.readlines())

def write_output(outfname):
    with open(outfname, "w") as f:
        for line in outf:
            f.write(line)
        
def main(inp):    
    lines = map(lambda a: a.split(" "), inp[1:])
    for line in lines:
        l = line[:]
        ncombos = int(l[0])
        combos = l[1:(ncombos+1)]
        combodic = {}
        for c in combos:
            combodic[c[0]+c[1]] = c[2]
            combodic[c[1]+c[0]] = c[2]
        noppos = int(l[ncombos+1])
        oppos = l[(ncombos+2):(ncombos+noppos+2)]
        oppodic = oppos[:]
        for o in oppos:
            oppodic.append(o[1] + o[0])
        seq = l[-1]
        sol = []
        for n in seq:
            if sol:
                if (n+sol[-1]) in combodic:
                    sol[-1] = combodic[(n+sol[-1])]
                else:
                    for e in sol:
                        if (n+e) in oppodic:
                            sol = []
                            break
                    else:
                        sol += n
            else:
                sol += n
                
        pout(str(sol).replace("'", ""))

inp = get_input(sys.argv[1])    
main(inp)
write_output(sys.argv[2])
    