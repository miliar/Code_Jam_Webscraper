inp = open('input.txt').readlines()
op = open('output.txt','w')
t = int(inp[0])
multDict = {'11':'1','1i':'i','1j':'j','1k':'k',
           'i1':'i','ii':'-1','ij':'k','ik':'-j',
           'j1':'j','ji':'-k','jj':'-1','jk':'i',
           'k1':'k','ki':'j','kj':'-i','kk':'-1'}
found = True
for i in range(t):
    tem1 = inp[2*i+1].split()
    l = int(tem1[0])
    x = int(tem1[1])
    text=''.join([inp[2*i+2][:-1]]*x)
    first = -1
    second = 0
    found = False
    while not found and first<len(text):
        sign = 1
        res = '1'
        for x in range(len(text)):
            res = multDict.get(res[-1]+text[x])
            if res[0]=='-':
                sign = sign * -1
            if res[-1] == 'i' and sign>0 and x>first:
                first = x
                break
        if x ==len(text)-1:
            break
        second = first+1
        res = '1'
        sign =1
        for x in range(first+1,len(text)):
            res = multDict.get(res[-1]+text[x])
            if res[0]=='-':
                sign = sign * -1
            if res[-1] == 'j' and sign>0 and x>=second:
                second = x
                break
            
        res = '1'
        sign = 1
        if x==len(text)-1:
            break
        for x in range(second+1,len(text)):
            res = multDict.get(res[-1]+text[x])
            if res[0]=='-':
                sign = sign * -1

        if res[-1] =='k' and sign==1:
            found = True

    if found:
        print("Case #"+str(i+1)+": YES\n")
        op.write("Case #"+str(i+1)+": YES\n")
    else:
        print("Case #"+str(i+1)+": NO\n")
        op.write("Case #"+str(i+1)+": NO\n")
        
    
    
            
    

op.close()
        
