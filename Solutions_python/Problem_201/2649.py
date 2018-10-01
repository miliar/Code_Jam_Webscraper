from sys import argv

INPUT_FILE = argv[1]
OUTPUT_FILE = argv[2]

with open(INPUT_FILE) as f1:
  with open(OUTPUT_FILE,'w') as f2:
    current = f1.readline()
    current = f1.readline()[:-1]
    case = 1
    while current!='':
      stalls,people = [int(x) for x in current.split(' ')]
      runs = [stalls]
      for n in range(people):
        total = runs.pop()
        if total%2:
          latest = [(total-1)/2,(total-1)/2]
          runs.extend(latest)
        else:
          latest = [total/2,total/2-1]
          runs.extend(latest)
        runs.sort()
      f2.write('Case #%d: %d %d\n'%(case,max(latest),min(latest)))
      case += 1
      current = f1.readline()[:-1]
