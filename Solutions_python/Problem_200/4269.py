for _ in xrange(input()):
    x=raw_input()
    p,f='',0
    for i in xrange(len(x)-1):
        if int(x[i])>int(x[i+1]):
            if p=='':
                x=x[:i]+str(int(x[i])-1)+'9'*(len(x)-i-1)
                break
            else:
                x=str(int(p))+'9'*(len(x)-i-1)
                break
        elif int(x[i])==int(x[i+1]):
            if f==0:
                p+=str(int(str(int(x[i])-1)+'9'))
                f=1
            else:
                p+='9'
    print "Case #"+str(_+1)+": "+str(int(x))
