j = open('A-large.out' , 'w')
f= open('A-large.in', 'r')
content = f.readlines()
content.pop(0)
a=0
for line in content:
    a+=1
    z=0
    arr= line.split()
    x = arr[0]
    y = arr[1]
    e = list(y) 
    w=0
    y=0
    for r in e:
            p = int(r)
            if p==0:
                w+=1
            else:
                
                if y>=w:
                    w+=1
                else:
                    b=w-y
                    w+=1
                    z+= b
                    y+= b
            y+=int(r)
        
    j.write('Case #'+ str(a) + ': ' + str(z))
    j.write('\n') 
j.close()

