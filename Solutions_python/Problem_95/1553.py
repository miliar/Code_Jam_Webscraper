cases = int(raw_input())
#     a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   u   v   w   x   y   z
t = ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']
for i in range(0,cases):
  ins = raw_input()
  ous = ''
  for j in list(ins):
    if (j == ' '):
      ous = ous + ' '
    else:
      ous = ous + t[ord(j)-97]

  print 'Case #' + str(i+1) + ': ' + ous
  
