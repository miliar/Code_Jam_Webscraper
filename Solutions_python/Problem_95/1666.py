fptr = open('A-small-attempt1.in','r')
fptr2=open('xyz.txt','w')

htab = {'\n':'\n',' ':' ','a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}

test_cases=fptr.readline()
i=1

for line in fptr:    
    case="Case #"+str(i)+": "
    fptr2.write(case)
    for ch in line:
        fptr2.write(htab[ch])
    i=i+1

fptr.close()
fptr2.close()




