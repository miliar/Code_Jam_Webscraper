l='welcome to code jam'
f = file('C-large.in')
fo = file('C-large.out','w')
line = f.readline()
i = 0
a = 0
b = 0
h =0
result = 0
number = 0
data=[]
tdata=[]
tmp1 =[]
tmp2 =[]
tmp3 =0
while line[i] <= '9' and line[i] >= '0' :    
   number = number * 10 + int (line[i])
   i +=1
N = number 

for y in range(N):
   a = 0
   b = 0
   data  = []
   tmp1  = []
   tmp2  = []
   tdata = []
   line = f.readline()
   
   for b in range(len(line)):
      if l[0] == line[b]:
         if b ==0:
            data = line
            break
         else:
            data = line[b:]
            break 
      b+=1
   b = len(data)-1
   while b >= 0:
      if l[len(l)-1] == data[b]:
         data = data[:b+1]
         break
      b-=1
   a = len(l)-1
   b = len(data)-1
   while b >= 0:
      if l[a]== data[b]:
         tdata.append(b)
         a-=1
         if a < 0 :
            break
         b-=1
      else:
         b-=1
   if len(tdata) < len(l):
      result = 0
   else:
      tmp5=[]
      result = 0
      for i in range(len(data)):
         tmp5.append(0)
      tmp1 = tmp5[:]
      tmp2 = tmp1[:]
      a = len(tdata)-2
      b = 0
      i = 0
      tmp3 =0
      while a > 0:
         i = tdata[a] -1
         while i >= 0:
            if data[i] == l[b]:
               if tmp2[i] ==0:
                  tmp3+=0
                  if b ==0:
                     tmp3+=1
               else:
                  tmp3+=tmp2[i]
            i-=1
         tmp1[tdata[a]] = tmp3
         tmp3 =0
         i = tdata[a] -1
         while i >= 0:
            if data[i] == l[b+1]:
               h = i
               while h >= 0:
                  if data[h] == l[b]:
                     if tmp2[h] ==0:
                        tmp3+=0
                        if b ==0:
                           tmp3+=1
                     else:
                        tmp3+=tmp2[h]
                  h-=1
               tmp1[i] = tmp3
               tmp3 =0
            i-=1
         tmp2 = tmp1[:]
         tmp1 = tmp5[:]
         a-=1
         b+=1
      tmp1 = []
      for i in range(len(tmp2)):
         if tmp2[i] != 0:
            tmp1.append(i)
      for i in range(len(tmp1)):
         result +=tmp2[tmp1[i]]      
      i = len(data)-2
      while i > 0 :
         if data[i] == l[len(l)-1]:
            for a in range(len(tmp1)):
               if i > tmp1[a]:
                  result+=tmp2[tmp1[a]]
         i-=1
   fo.write('Case #%d: %04d\n'%(y+1,result%10000))
f.close