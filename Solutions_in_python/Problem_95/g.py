
num=0

file=open('input.txt','r')
output=open('output.txt','w')
file.read(2)




def eachline(strLine):
    dictr={' ':' ','':' ','\n':'\n','z':'q','q':'z','e':'o','j':'u','p':'r','m':'l','y':'a','s':'n','l':'g','j':'u','c':'e','k':'i','d':'s','x':'m','v':'p','n':'b','r':'t','i':'d','b':'h','t':'w','a':'y','h':'x','w':'f','f':'c','o':'k','u':'j','g':'v'}
    
    
    newstrline=''
    for char in strLine:
        
        newstrline=newstrline+dictr[char]
    return newstrline
   
for line in file:
    num=num+1
 
    l='Case #'+ str(num)+': '+ eachline(line)
    output.write(l)
file.close()
output.close()



