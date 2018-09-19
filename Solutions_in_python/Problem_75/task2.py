#!/usr/bin/python -tt

import sys

def doWork(combineList, opposedList, invoke): 
  #if len(invoke) == 1: 
  #  return invoke

  answer = []
  for i in invoke: 
    answer.append(i)
    flag = True
    if (len(answer) > 1): 
      for (x, y, z) in combineList: 
        if answer[-1] == x and answer[-2] == y or answer[-1] == y and answer[-2] == x: 
          answer.pop(-1)
          answer.pop(-1)
          answer.append(z)
          flag = False
    if flag == True: 
      for j in answer[:-1]: 
        if (i, j) in opposedList or (j, i) in opposedList: 
          answer = []
  
  out = '['
  for i in answer: 
    out += i
    out += ', '
  out = out[:-2]
  out += ']'
  if len(answer) > 0:
    return out
  else:
    return answer


def main():
  f = open("B-large.in", 'rU')
  lines = f.readline()
  
  output = open('output', 'w')
  for i in range(int(lines)):
    line = f.readline().split(" ")
    combine = []
    opposed = []
    invoke = [ x for x in line[-1][:-1]]
    for j in range(int(line[0])): 
      combine.append(line[j+1])
    for j in range(int(line[int(line[0])+1])): 
      opposed.append(line[j+int(line[0])+2])
    
    combine = [(x, y, z) for (x, y, z) in combine]
    #tmp = [(y, x, z) for (x, y, z) in combine]
    #combine.extend(tmp)
    
    opposed = [(x, y) for (x, y) in opposed] 
    #tmp = [(y, x) for (x, y) in opposed]
    #opposed.extend(tmp)
    
    #print combine
    #print opposed
    #print invoke
    #print doWork(combine, opposed, invoke)
    output.write("Case #"+(str(i+1))+": ")
    output.write(str(doWork(combine, opposed, invoke)))
    output.write("\n")
  f.close()
  output.close()
  
if __name__ == '__main__':
  main()
