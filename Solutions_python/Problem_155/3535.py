
# Google Code Jam 2015
# Qualification Round 2015
# Problem A. Standing Ovation

def process_case(line):
  # Number of Friends Required For Standing Ovation
  nofr = 0
  # Current People Clapping
  cpc = 0
  # Current Shyness Level (based on index)
  csl = 0
  # print(line)
  # Shyness max
  Smax = int(line[0:1])
  # Audience Shyness Array
  # index = shyness level (starting with 0)
  # value = number of audience members with said shyness of said index level
  Sarray = []
  #print 'Char 2: %i' % int(line[2])
  for j in xrange(2, Smax+3):
    try:
      Sarray.append(int(line[j]))
    except:
      pass
    #print '%i: %i (shy)' % (j-2, int(line[j]))
  #print 'Smax: %i' % Smax
  #print 'Sarray:'
  #print(Sarray)
  for csl in xrange(0, len(Sarray)):
    while csl > cpc + nofr:
      nofr += 1
    cpc += Sarray[csl]
  return nofr

def main():
  #print('hello')
  filename_in = 'A-small-attempt0.in'
  filename_out = 'A-small-attempt0.out'
  # Number of Cases
  noc = 0
  # Number of Friends Required
  nofr = 0
  # Friends Required For Standing Ovation in Case
  fhi = open(filename_in, 'rb')
  fho = open(filename_out, 'w+')
  line = fhi.readline()
  noc = int(line)
  #print(noc)
  for i in xrange(0, noc):
    line = fhi.readline()
    nofr = process_case(line)
    print('Case #%i: %i' % (i + 1, nofr))
    fho.write('Case #%i: %i\n' % (i + 1, nofr))
  fho.close()
  fhi.close()

if __name__ == '__main__':
  main()
