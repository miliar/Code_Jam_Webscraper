def sol(lines):
 out=[]; outline=None
 for line in lines:
  if set(line)==set(['?']): out.append(outline)
  else:
   letters=sorted([(line.index(let),let) for let in list(set(line)-set(['?']))])
   outline=letters[0][1]*letters[0][0]; letters.append((len(line),''))
   for i in range(len(letters)-1): outline+=letters[i][1]*(letters[i+1][0]-letters[i][0])
   out.append(outline)
 if out[0]==None:
  i=0
  while out[i]==None: i+=1
  for j in range(i): out[j]=out[i]
 return '\r\n'.join(out)

inp=file('A-large.in','rb+'); out=file('A-large.out','wb+')
for t in range(1,int(inp.readline().strip())+1):
 R,C=inp.readline().strip().split(' '); R=int(R); C=int(C)
 caselines=[inp.readline().strip() for r in range(R)]
 out.write('Case #%i:\r\n%s\r\n'%(t,sol(caselines)))