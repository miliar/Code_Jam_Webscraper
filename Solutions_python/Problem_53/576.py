a = file('input2.txt').readlines()
s = ''
k = 1
for i in a[1:]:
    a,b = i.split()
    a = int(a)
    b = int(b)
    if (b+1) % pow(2,a) ==0:
            s += 'Case #'+str(k)+': ON\n'
    else:
            s += 'Case #'+str(k)+': OFF\n'
    k+=1
w = open("output.txt",'w')
w.write(s)
w.close()
print 'done'

