from sys import argv
import math

INPUT_FILE = argv[1]
OUTPUT_FILE = argv[2]

def oscillate(l):
    splitting = int(math.ceil(len(l)/2))
    first_half = l[:splitting]
    second_half = l[splitting:]
    new_results = [False]*total
    for i,n in enumerate(first_half):
      new_results[2*i] = n
    for i,n in enumerate(second_half):
      new_results[2*i+1] = n
    return new_results

with open(INPUT_FILE) as f1:
  with open(OUTPUT_FILE,'w') as f2:
    current = f1.readline()
    current = f1.readline()[:-1]
    case = 1
    while current!='':
      totals = {}
      total,r,o,y,g,b,v = [int(q) for q in current.split(' ')]
      totals['R'] = r
      totals['O'] = o
      totals['Y'] = y
      totals['G'] = g
      totals['B'] = b
      totals['V'] = v
      if max(r,y,b)>total/2:
        answer = 'IMPOSSIBLE'
      else:
        stringed = []
        for k in sorted(totals.keys(),key=lambda x:-totals[x]):
          for n in range(totals[k]):
            stringed.append(k)
        assignments = oscillate(stringed)
        answer = ''.join(assignments)
      f2.write('Case #%d: %s\n'%(case,answer))
      case += 1
      current = f1.readline()[:-1]
