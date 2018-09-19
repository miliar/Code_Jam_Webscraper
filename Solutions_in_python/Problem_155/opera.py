fd = open("A-small-attempt0.in.txt")
fd1 = open("opera_output.txt","w")
line = fd.readline()
no_testcase = int(line)
i = 0
while i < no_testcase:
  i += 1
  pos = 0
  mem = 0
  cnt = 0
  tot = 0
  line = fd.readline()
  #print line
  inp  = line.split()
  shy  = inp[1]
  #print shy
  for s in shy:
     cnt = int(s)
     #print cnt, tot, pos, mem
     if  cnt and tot < pos:
        mem +=  (pos - tot)
        tot += mem
     tot += cnt
     pos += 1 
     
  #print mem
  #print("Case #%i: %i  " % ((i), (mem)))
  fd1.write("Case #%i: %i\n" % ((i), (mem)))
fd.close()
fd1.close()
