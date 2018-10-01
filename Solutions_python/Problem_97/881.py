def uniq(seq, idfun=None): 
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result

f=open("C-small-attempt0.in").readlines()

#f="""4
#1 9
#10 40
#100 500
#1111 2222""".splitlines()

"""
"""

#f="50\n" + "\n".join(["100 999" for x in range(50)])
#f=f.splitlines()

def go():
  i_lines = [x.strip() for x in f]
  case_count=int(i_lines[0])
  i_lines = i_lines[1:]
  assert case_count==len(i_lines)
  numbers = [aline.split(' ') for aline in i_lines]
  casenumber = 1
  the_results=[]
  for pair in numbers:
    this_count = 0
    A,B = pair
    a,b = (int(A),int(B)+1)
    for n in [x for x in range(a,b)]:
      N=str(n)
      lenN=len(N)
      perms=[N[x:] + N[:x] for x in range(1,lenN)]
      for m in [x for x in range(n+1,b)]:
        M=str(m)
        if M in perms:
          this_count += 1
    the_results.append(this_count)
  return '\n'.join(["Case #%i: %i" % (x,y) for (x,y) in zip(range(1,len(the_results)+1),the_results)])


open('C-small-attempt0.out','w').write(go())


