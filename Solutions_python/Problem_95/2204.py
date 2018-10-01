file=open("input.txt", 'r')


dict={'a':'y','b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x',
      'i':'d','j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r',
      'q':'z','r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m',
      'y':'a', 'z':'q'}

input=iter(file)
X=input.readline()
str=''
for a,i in enumerate(input):
    str=''
    for j in i:
     if j==' ':
         str+= ' '
     elif j=='\n':
         break
     else: 
         str+=dict[j]
    print "Case #%d: %s" % (a+1, str) 

file.close()
