inFileName = 'C-small-attempt1 (1).in'
#inFileName = 'sample.in'

inFile = open(inFileName,'r')
outFile = open(inFileName.replace('.in','.out'),'w')

N = int(inFile.readline().strip())

for m in range(N):
  lis = []
  l = inFile.readline().strip().split(' ')
  start = int(l[0])
  end = int(l[1])
  for k in range(start,end+1):
    for i in range(len(str(k))):
      a = int(str(k)[i:] + str(k)[:i])
      if(a <= end) and (a>=start) and (a < k) and (a!=k) and (len(str(a)) == len(str(k))) and ([k,a] not in lis) and ([a,k] not in lis):
        lis.append([k,a])
        #outFile.write('Case #' + str(m+1) + ': ' + str(k) + ',' + str(a) + '\n')
  outFile.write('Case #' + str(m+1) + ': ' + str(len(lis)) + '\n')
  #print '\n'.join(map(str,lis))

