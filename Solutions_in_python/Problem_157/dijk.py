def mult(a,b):
    if a=='1':
        return b
    elif b=='1':
        return a
    elif a[0]=='-' and b[0]=='-':
        return mult(a[1],b[1])
    
    elif a=='i':
        if b=='i':
            return '-1'
        elif b=='j':
            return 'k'
        elif b=='k':
            return '-j'
        elif b[0]=='-':
            c='-'+mult(a,b[1])
            i=0
            n=len(c)
            while i<len(c)-1 and c[i+1]=='-':
                c=c[i+2:n]
            return c
        
    elif a=='j':
        if b=='i':
            return '-k'
        elif b=='j':
            return '-1'
        elif b=='k':
            return 'i'
        elif b[0]=='-':
            c='-'+mult(a,b[1])
            i=0
            n=len(c)
            while i<len(c)-1 and c[i+1]=='-':
                c=c[i+2:n]
            return c
        
    elif a=='k':
        if b=='i':
            return 'j'
        elif b=='j':
            return '-i'
        elif b=='k':
            return '-1'
        elif b[0]=='-':
            c='-'+mult(a,b[1])
            i=0
            n=len(c)
            while i<len(c)-1 and c[i+1]=='-':
                c=c[i+2:n]
            return c
        
    elif a[0]=='-':
            c='-'+mult(a[1],b)
            i=0
            n=len(c)
            while i<len(c)-1 and c[i+1]=='-':
                c=c[i+2:n]
            return c
    
T=int(input())
i=0
while i<T:
    b=[]
    l_x=[int(k) for k in input().split(' ')]
    string=str(input())
    l=l_x[0]
    x=l_x[1]
    multp=string*x
    j=0
    n=len(multp)
    prod1='1'
    prod2='1'
    prod3='1'
    continuar=True
    out='NO'
    """
    while j<n:
        prod1=mult(prod1,multp[j])
        if prod1[len(prod1)-1]=='i' or prod1[len(prod1)-1]=='j' or prod1[len(prod1)-1]=='k':
            b.append(prod1)
        j=j+1
    if prod1=='-1':
        aux=[]
        m=len(b)
        while len(b)>3:
            prod1='1'
            k=0
            while k<m:
                prod1=mult(prod1,b[j])
                if prod1[len(prod1)-1]=='i' or prod1[len(prod1)-1]=='j' or prod1[len(prod1)-1]=='k':
                    aux.append(prod)
                k=k+1
            b=aux
            aux=[]
        
        if n>=3:
            out='YES'
                
    """
    while True:
        while j<n and prod1!='i' :#or (prod1[len(prod1)-1]=='i' and continuar==True):
            continuar=False
            prod1=mult(prod1,multp[j])
            j=j+1
        if prod1[len(prod1)-1]=='i':
            if j==n:
                break
            prod2='1'
            continuar2=True
            k=j
            while True:
                while (k<n and prod2!='j') :#or (prod2[len(prod2)-1]=='j' and continuar2==True):
                    continuar2=False
                    prod2=mult(prod2,multp[k])
                    k=k+1
                if prod2[len(prod2)-1]=='j':
                    if k==n:
                        continuar=True
                        break
                    prod3='1'
                    l=k
                    while l<n:
                        prod3=mult(prod3,multp[l])
                        l=l+1
                    if prod3[len(prod3)-1]=='k':
                        if prod1[0]!='-':
                            if prod2[0]!='-':
                                if prod3[0]!='-':
                                    out='YES'
                                    break
                                else:
                                    break
                                    #continuar2=True
                                    #continue
                            else:
                                if prod3[0]=='-':
                                    out='YES'
                                    break
                                else:
                                    break
                                    #continuar2=True
                                    #continue
                        else:
                            if prod2[0]!='-':
                                if prod3[0]!='-':
                                    break
                                    #continuar2=True
                                    #continue
                                else:
                                    out='YES'
                                    break
                            else:
                                if prod3[0]!='-':
                                    out='YES'
                                    break
                                else:
                                    break
                                    #continuar2=True
                                    #continue
                    else:
                        break
                        #continuar2=True
                        #continue
                else:
                    #continuar=True
                    break
            if out=='YES':
                break
            else:
                break
        else:
            break
    
    print('Case #'+str(i+1)+': '+out)
    i=i+1
