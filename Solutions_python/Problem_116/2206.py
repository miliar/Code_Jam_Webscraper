infile=open('A-large.in','r')
try :
   outfile=open('output.txt','w')
except :
   outfile=open('output.txt','x')

def full(a):
   for i in range(0,4):
      for j in range(0,4):
         if a[i][j]=='.':
            return False
   return True

def test(st):
   s=0
   for i in range(0,4):
      if st[i]=='O' or st[i]=='T':
         s+=1
   if s==4:
      return 0
   s=0
   for i in range(0,4):
      if st[i]=='X' or st[i]=='T':
         s+=1
   if s==4:
      return 1
   return -1

def find(a):
   for i in range(0,4):
      s=''
      for j in range(0,4):
         s+=a[i][j]
      x=test(s)
      if x==0:
         return 'O'
      if x==1:
         return 'X'
   for j in range(0,4):
      s=''
      for i in range(0,4):
         s+=a[i][j]
      x=test(s)
      if x==0:
         return 'O'
      if x==1:
         return 'X'
   s=''
   for i in range(0,4):
      s+=a[i][i]
   x=test(s)
   if x==0:
      return 'O'
   if x==1:
      return 'X'
   s=''
   for i in range(0,4):
      s+=a[i][3-i]
   x=test(s)
   if x==0:
      return 'O'
   if x==1:
      return 'X'
   return ''

st=infile.readline()
n=int(st)
for i in range(0,n):
   a=[[None for x in range(0,5)] for x in range(0,5)]
   for j in range(0,4):
      st=infile.readline()
      st=st.replace('\n','')
      for k in range(0,4):
         a[j][k]=st[k]
   f=find(a)
   ff=full(a)
   st='Case #'+str(i+1)+': '
   outfile.write(st)
   if f=='O':
      outfile.write('O won')
   elif f=='X':
      outfile.write('X won')
   elif f=='' and ff:
      outfile.write('Draw')
   else:
      outfile.write('Game has not completed')
   outfile.write('\n')
   infile.readline()

infile.close()
outfile.close()
