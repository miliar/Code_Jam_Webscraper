# @author Carlos M. Pascal 
# @email cpascal at ac.tuiasi.ro


def comp(max, conf):
  sum = int(conf[0])
  no_friend = 0
  for index in range(1, max+1):
    no_person = sum + no_friend
    if no_person < index:
      no_friend += index-no_person
    sum+= int(conf[index])
  return no_friend


def doWork(input, output):
  fin = open(input)
  fout = open(output, 'w')
  no_cases = int(fin.readline())
  no = 1
  for line in fin:
    max, conf = line.split()
    no_friend = comp(int(max), conf)
    msg = 'Case #{0}: {1}\n'.format(no, no_friend)
    #print msg
    fout.write(msg)
    no+=1
  fin.close()
  fout.close()

input = 'D:\work\codejam2015\inprAs.txt'
output = 'D:\work\codejam2015\outprAs.txt'
doWork(input, output)

  
"""  
case1 = '4 11111'
case2 = '1 09'
case3 = '5 110011'
case4 = '0 1'
"""

  
""" 
def main():
   
# Un tipar standar pentru apelare main()
if __name__ == '__main__':
  main()
"""
    