t = ['y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q']

def convert(G):
   gres = [''] * 100
   for i, c in enumerate(G):
      if not c == ' ':
         gres[i] = t[ord(c) - 97]
      else:
         gres[i] = ' '

   return ''.join(gres)

f = open('/home/blessedchild/Desktop/Jam/tmp.txt', 'r')

num = int(f.readline())

i = 1
res = ''
for l in range(num):
   res += 'Case #{0}: {1}'.format(i, convert(f.readline().rstrip()))
   if l < (num - 1):
      res += '\n'
      i += 1

f.close()

print(res, end='')
