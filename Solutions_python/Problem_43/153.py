import sys
def get_lines(fname):
  fDes=open(fname,'r')
  lines=[]
  for i in fDes.read().split('\n'):
    lines.append(i)
  lines=filter(lambda x:x,lines)
  return lines


def parse_lines(lines):
  pointer=1
  cases=int(lines[0])
  for j in range(1,cases+1):
    case=lines[j]
    print "Case #"+str(j)+": "+str(solve(case))

def solve(case):
    digits=list(case)
    digits2=[]
    store={}
    store[digits[0]]=1
    digits2.append(1)
    counter=0
    if len(digits)>1:
        for i in digits[1:]:
            if not store.has_key(i):
                if counter==1: counter+=1
                store[i]=counter
                digits2.append(counter)
                counter+=1
            else:
                digits2.append(store[i])
    #print digits2
    base=len(store)
    if base==1: base=2
    sum=0;power=1
    for i in reversed(digits2):
        sum+=i*power
        power*=base
    return sum



if __name__=="__main__":
    parse_lines(get_lines(sys.argv[1]))
