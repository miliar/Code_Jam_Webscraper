import sys

def find_num_friends(x):
  if x[0] == '0':
    return 0
  
  x = x.split()[1]
  friends_invited = 0
  cumulative_friends = 0
  for i in range(len(x)):
    if i > cumulative_friends:
      friends_invited += (i - cumulative_friends)
      cumulative_friends = i
    cumulative_friends += int(x[i])
  return friends_invited

if __name__ == '__main__':
  infile = sys.argv[1]
  #print 'reading ' + infile
  infile = open(infile)
  num_tests = int(infile.readline())
  #print 'there are %d tests' % num_tests
  outfile = open('q1_soln.txt','w')
  for i in range(num_tests):
    num_friends = find_num_friends(infile.readline().rstrip())
    outfile.write('Case #%d: %d\n' % (i+1,num_friends))
  outfile.close()
  #print 'success'
