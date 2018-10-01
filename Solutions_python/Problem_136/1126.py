f = open('Google Cookie Clicker Alpha Large.in','r')
g = open('Google Cookie Clicker Alpha Large.out','w')

def should_buy_farm(C,F,X,cookies,freq):
    dontbuy = (X-cookies)/float(freq)
    b1 = (C-cookies)/float(freq)
    c1 = cookies + freq*b1
    c1 -= C
    b2 = (X-c1)/float(freq+F)
    buy = b1+b2
    if dontbuy < buy:
        return False
    else:
        return True
    
    

def best_buy(C,F,X):
    cookies = 0.0
    freq = 2.0
    t = 0.0
    while True:
        if cookies >= X:
            break
        if should_buy_farm(C,F,X,cookies,freq):
            t1 = (C-cookies)/float(freq)
            cookies += t1*freq
            cookies -= C
            freq += F
        else:
            t1 = (X-cookies)/freq
            cookies += t1*freq
        t += t1
    return '%.7f' %t

def Google_print(filename,answers):
    for i in range(len(answers)):
        filename.write("Case #%s: %s\n" % (str(i+1),answers[i]))
        print "Case #%s: %s" % (str(i+1),answers[i])
    return

cases = int(f.readline())
answers = []
for i in range(cases):
    r = f.readline().rstrip().split(' ')
    C,F,X = [float(x) for x in r]
    answers.append(best_buy(C,F,X))

Google_print(g,answers)
f.close()
g.close()

    

        
        
            
       
            
        
        
