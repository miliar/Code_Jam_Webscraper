__author__ = 'Sirna'

fname = "a.in"
o = open("a.out","w")
with open(fname) as f:
    content = f.readlines()
    content = [x.strip('\n') for x in content]
    cases = int(content[0])
    #cases =1
    for i in range(cases):
        aud,shylevel = content[i+1].split()
        #shylevel="0110001"
        last = int(aud)+1
        ans = 0
        counter = 0
        if(shylevel[0]=='0'):
            counter=1
            ans =1
        else:
            counter = int(shylevel[0])
        for j in range(1,last):
           if(counter<j):
                ans+= j-counter
                counter+=ans
           else:
                if(counter==j and j!=last and shylevel[j]=='0'):
                    ans+=1
                    counter+=1
                else:
                    counter+= int(shylevel[j])
        o.write("Case #"+str((i+1))+": "+str(ans)+"\n")
    o.close()
