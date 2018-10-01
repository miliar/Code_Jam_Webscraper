import math  

t = int(raw_input())


# inp = open('C-large.in', 'r')
# outf = open('c.out', 'w')
# t = int(inp.readline())


for i in xrange(1, t + 1):
  rl = (raw_input()).split(" ")

  # rl = (inp.readline()).split(" ")

  y = int(rl[0].strip())
  z = int(rl[1].strip())
  di = {y:1}
  out = [0,0]
  while(1):
    if di[max(di)] < z :
      step = di[max(di)]
    else :
      step = z
    # print ("{}".format(di))
    if(step/2) > 0:
      to_step1 = step/2
    else:
      to_step1 = 1
    if(step/2)-1>0:
      to_step2 = (step/2) -1
    else:
      to_step2 = 1

    if (max(di)/2 in di):
      di[max(di)/2] += step
    else:
      di[max(di)/2] = step
    out[0] = max(di)/2
    # print (">> {}".format(di))
    if(max(di) % 2 == 0):
      # print max(di)/2 - 1
      if(max(di)/2 - 1 in di):
        di[max(di)/2 - 1] += step
      else:
        di[max(di)/2 - 1] = step
      out[1] = max(di)/2 - 1
    else: 
      # print max(di)/2
      if (max(di)/2 in di):
        di[max(di)/2] += step
      else:
        di[max(di)/2] = step
      out[1] = max(di)/2
    di[max(di)] -= step
    z -= step
    
    if di[max(di)] == 0:
      del di[max(di)]
    # print (">> {} z={} step={} out={}".format(di, z, step, out ))
    
    if (z == 0):
      break


    # print (">>> {}\n".format(di))
    # li = list(set(li))
    # print li

    # print "----"
  
  print ("Case #{}: {} {}".format(i, max(out), min(out)))
  # outf.write ("Case #{}: {} {}\n".format(i, max(out), min(out)))
    