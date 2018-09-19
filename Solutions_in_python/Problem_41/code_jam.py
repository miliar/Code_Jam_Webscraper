
def perm(l):
    sz = len(l)
    if sz <= 1:
        return [l]
    return [p[:i]+[l[0]]+p[i:] for i in xrange(sz) for p in perm(l[1:])]


f = open('/home/norman/Desktop/new/input', 'r')
h = open('/home/norman/Desktop/new/output', 'w')

number_inputs = int(f.readline())
for gg in range(number_inputs):



  string = f.readline() #"aabacbca" #"aabaaadsfbsnfbjksfdcsa,nbds,a,anbsdc,bnad,cba,bcabcbascbndsabc,abc"
  the_input = []
  for ii in range (0,len(string)-1):
    the_input.append(string[ii])

  new_list_1 = perm(the_input)
  the_input.append(0)
  
  new_list_2 = perm(the_input)
  
  new_list_1 = new_list_1 + new_list_2
  all_perts = []  

  for ii in new_list_1:
    number = 0
    length_of_number = len(ii)
    for jj in ii:
      number = number + int(jj) * 10**(length_of_number-1)
      length_of_number = length_of_number - 1
    all_perts.append(number)
    
  difference = []
  for ii in all_perts:
    difference.append(ii- int(string))
  mini = 10**20
  for ii in difference:
    if ii > 0 and ii < mini:
      mini = ii
  
  marker = 0
  for ii in difference:
    if ii == mini: break
    marker = marker + 1
    
  final_answer = "Case #" + str(gg+1) + ": " + str(all_perts[marker]) + "\n"


  h.write (final_answer)

