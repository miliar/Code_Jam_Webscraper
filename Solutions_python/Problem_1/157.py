#!/usr/local/bin/python
#set-encoding=UTF-8

import fileinput

def look4LastEngineFromPos(engines, queries, inipos):
   retval = -1
   lstlen = len(queries)
   nextpos = []
   for engine in engines:
      index = inipos
      while index < lstlen and engine <> queries[index]:
         index += 1
      if index == lstlen:
         nextpos.append(-1)
         return -1
      else:
         nextpos.append(index)
   
   for number in nextpos:
      if number == -1:
         retval = number
         break
      else:
         if number > retval:
            retval = number
   
   return retval


problems = 0
nproblem = 0
engines  = 0
cengine  = 0
queries  = 0
cquery   = 0
earray   = []
qarray   = []
nswitch  = 0
if __name__ == "__main__":
   
   for line in fileinput.input():
      if fileinput.isfirstline():
         # Fist-line
         problems = int(line.strip('\n'))
      
      if 1<fileinput.filelineno() and nproblem < problems:
         if engines == 0:
            engines = int(line.strip('\n'))
            cengine = engines
         elif cengine > 0:
            earray.append(line.strip('\n'))
            cengine -= 1
         elif queries == 0:
            queries = int(line.strip('\n'))
            cquery  = queries
            if cquery == 0:
               nproblem += 1
               print "Case #%d: %d" % (nproblem, nswitch)
               engines = 0
               cengine = 0
               del earray[:]
         elif cquery > 0:
            qarray.append(line.strip('\n'))
            cquery -= 1
            if cquery == 0:
               #Look 4 the number of switches
               pos = 0
               pos = look4LastEngineFromPos(earray, qarray, pos)
               while pos <> -1:
                  nswitch += 1
                  pos = look4LastEngineFromPos(earray, qarray, pos)
               nproblem += 1
               print "Case #%d: %d" % (nproblem, nswitch)
               engines = 0
               cengine = 0
               queries = 0
               cquery  = 0
               nswitch = 0
               del earray[:]
               del qarray[:]
