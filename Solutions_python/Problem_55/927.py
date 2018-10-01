# sinnick
# hc svnt dracones

import sys
import math

def solution(str):
  lines = str.splitlines()
  testcount = int(lines[0])
  s = ""
  for i in range(testcount):
    s += "Case #%d: " % (i+1)
    (R, k, N) = lines[i*2+1].split(" ")
    R = int(R)
    k = int(k)
    N = int(N)
    queue = [int(x) for x in lines[i*2+2].split(" ")]
    originalqueue = queue[:]
    total = 0
    interimvalues = {}
    detected = -1
    for run in range(R):
      if (queue == originalqueue and run > 0):
        detected = run
        break
      spaceleft = k
      coaster = []
      while (len(queue) > 0 and spaceleft >= queue[0]):
        val = queue.pop(0)
        coaster.append(val)
        total += val
        interimvalues[run] = total
        spaceleft -= val
      queue.extend(coaster)

    if (detected >= 0):
      multiples = math.floor(R / (detected))
      remainder = R % (detected)
      total = multiples*total
      if (remainder != 0):
        total += interimvalues[remainder - 1]

    s += "%d\n" % total

  return s.strip()

if __name__ == "__main__":
#  i,o = open("A.in", "r"), sys.stdout
#  i,o = open("A-test.in","r"), open("A-test.out","w")
  i,o = open("C-small-attempt0.in","r"), open("C-small-attempt0.out","w")
#  i,o = open("A-small-attempt1.in","r"), open("A-small-attempt1.out","w")
#  i,o = open("A-small-attempt2.in","r"), open("A-small-attempt2.out","w")
#  i,o = open("A-large.in","r"), open("A-large.out","w")

  input = i.read()
  result = solution(input)
  o.write(result)