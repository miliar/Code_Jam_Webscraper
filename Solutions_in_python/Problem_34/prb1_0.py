import re
import sys
fDes=open(sys.argv[1],'r')
lines=[]
win_newLine='\n'
for i in fDes.read().split(win_newLine):
  lines.append(i)


lines=filter(lambda x: x,lines)

params=lines[0].split(' ')
word_size=int(params[0])
words_num=int(params[1])
expressions_num=int(params[2])

words=lines[1:words_num+1]
expressions=lines[words_num+1:]

expr_counter=0
for expr in expressions:
  expr_counter+=1
  expr=expr.replace('(','[')
  expr=expr.replace(')',']')
  regex=re.compile(expr)
  counter=0
  for word in words:
    if regex.match(word):
      counter+=1
  output= "Case #"+str(expr_counter)+": "+str(counter)
  print output
