#!/usr/bin/env python
#By Jai Dhyani
#Automatically generated on 2011-05-07

class Case:
    opposed_pairs=[]
    transforms=dict()
    stack=[]
    eles=set()

def st(s):
    return tuple(sorted(list(s)))

if __name__ == "__main__":
    files=['test','B-small-attempt0']
    for file in files:
        f=open('%s.in'%file)
        o=open('%s.out'%file,'w')
        num_trials=int(f.readline())
        for i,trial in enumerate(xrange(num_trials)):
            vals=f.readline().strip().split(' ')
            c=int(vals[0])
            transforms=vals[1:1+c]
            d=int(vals[1+c])
            opposed_pairs=set([st(p) for p in vals[2+c:2+c+d]])
            n=int(vals[2+c+d])
            to_invoke=list(vals[3+c+d])
            t_dict=dict()
            for t in transforms:
                elems=st(t[:2])
                t_dict[tuple(elems)]=[t[2]] 
            def transform(l):
                while tuple(sorted(l[-2:])) in t_dict:
                    l=l[:-2]+t_dict[tuple(sorted(l[-2:]))]
                return l
            chain=[]
            for e in to_invoke:
                chain.append(e)
                chain=transform(chain)
                for x in chain[:-1]:
                    if tuple(sorted([x,chain[-1]])) in opposed_pairs:
                        chain=[]
                        break
            print 'Case #%d: [%s]'%(i+1,', '.join(e for e in chain))
            o.write('Case #%d: [%s]\n'%(i+1,', '.join(e for e in chain)))
        o.close()
        f.close()


