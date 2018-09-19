#!c:\pypy-2.0-beta2\pypy.exe

import itertools
import fileinput

class tickets_group(object):
    def __init__(self,origin,end,p):
        self.origin=origin
        self.end=end
        self.p=p
    def trade_tickets(self,other_group):
        if other_group.origin > self.end or other_group.end < self.origin or self.p == 0 or other_group.p == 0:
            return (0,[])
        deltaE = (self.end-other_group.end)
        deltaO = (self.origin-other_group.origin)
        gain_from_switching_a_ticket = deltaO*deltaE
        if gain_from_switching_a_ticket > 0:
            # Switching tickets - min(self.p,other.p) of the people now travel "other.origin->self.end", p of the people now travel "self.origin->other.end", the rest remain in their original routing (if self.p was smaller than other.p, the other will have some left. Otherwise, the self group will have few remaining)
            new_p_groups = min(self.p,other_group.p)
            new_group1 = tickets_group(self.origin,other_group.end,new_p_groups)
            new_group2 = tickets_group(other_group.origin,self.end,new_p_groups)
            self.p -= new_p_groups
            other_group.p -= new_p_groups
            return ((gain_from_switching_a_ticket*new_p_groups),[new_group1,new_group2])
        else:
            return (0,[])
    def __repr__(self):
        return "tickets_group("+repr(self.origin)+","+repr(self.end)+","+repr(self.p)+")"

def run_train(coordinates_list):
    group_of_groups = [tickets_group(o,e,p) for (o,e,p) in coordinates_list]
    current_gain = 1
    total_gain = 0
    while current_gain > 0:
        current_gain = 0
        new_group_of_groups = []
        for p in itertools.combinations(group_of_groups,2):
            #print "Trading:",repr(p)
            (gain,new_groups) = p[0].trade_tickets(p[1])
            #print gain,repr(new_groups),repr(p)
            if gain > 0:
                new_group_of_groups += list(new_groups)
                current_gain += gain
        group_of_groups = [x for x in (group_of_groups+new_group_of_groups) if x.p > 0]
        total_gain += current_gain
        #print repr(group_of_groups),total_gain
        total_gain = total_gain % 1000002013
    return total_gain

#run_train([(1,5,1),(2,4,1),(3,6,2)])

def run_case(it):
    (N,M) = [int(x) for x in it.next().split()]
    entries = []
    for i in range(M):
        entries.append([int(x) for x in it.next().split()])
    return run_train(entries)

def main():
    it = fileinput.input()
    num_cases = int(it.next())
    for i in range(num_cases):
        print "Case #%d: %d"%(i+1,run_case(it))

if __name__ == "__main__":
    main()
