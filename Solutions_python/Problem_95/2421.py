def googl(fin):
  #dic = {}
  o = 0
  compa = {'y':'a','n':'b','f':'c','i':'d','c':'e','w':'f','l':'g','b':'h','k':'i','u':'j','o':'k','m':'l','x':'m','s':'n','e':'o','v':'p','z':'q','p':'r','d':'s','r':'t','j':'u','g':'v','t':'w','h':'x','a':'y','q':'z'}
  a = ""
  c = 1
  while fin!='':
    #print c
    #print fin
    if fin[0]==' ': a+= ' '
    elif fin[0]!= ' ':
      a = a + compa[fin[0]]
    fin = fin[1:]
    #c+=1
  return a

def main():
  t = int(raw_input())
  for i in range(1,t+1):
    line = raw_input()
    print "Case #" + str(i) + ": " + googl(line)
    
main()
