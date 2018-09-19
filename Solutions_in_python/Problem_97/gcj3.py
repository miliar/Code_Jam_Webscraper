import sys
f=open(sys.argv[1]).read()
f_lines = f.split('\n')
pairs_dict={}

def get_num_pairs(num,A,B):
  count=0
  #print num 
  num_str=str(num)
  for i in range(0, len(num_str)):
    #print num_str[len(num_str)-1-i:len(num_str)], num_str[0:len(num_str)-1-i]
    new_str = num_str[len(num_str)-1-i:len(num_str)]+num_str[0:len(num_str)-1-i]
    m=int(new_str)
    if num<m and (num>A or num==A) and (m<B or m==B):
      #print int(new_str),
      count=count+1
      key=str(num)+","+str(m)
      if key in pairs_dict:
        pairs_dict[key]+=1
      else:
        pairs_dict[key]=1
  #print "\n================"
  return count

def get_num_recycled(A,B):
  super_count=0
  for i in range(A, B+1):
    super_count= super_count+get_num_pairs(i,A,B)
  return super_count

num_times=int(f_lines[0])
for i in range(0, num_times):
   pairs_dict={}
   line_split = f_lines[i+1].split(" ")
   A = int(line_split[0])
   B = int(line_split[1])
   get_num_recycled(A,B)
   print "Case #"+str(i+1)+": "+str(len(pairs_dict.keys()))
   #print pairs_dict

