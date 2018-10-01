import sys
f= open("input.txt",'r');
out = open('out.txt','w');

orig_stdout = sys.stdout

sys.stdout = out

T = int(f.readline());
def takeinput():
    global f;
    a=[];
    b=[];
    for i in range(0,4):
        finput = f.readline().rstrip();
        b = [ int(n) for n in finput.split(" ")];
        a.append(b);
    return a;

    
    


for i in range(0,T):
    a1 = int(f.readline());
    a = takeinput();
    c1 = a[a1-1];
    b1 = int(f.readline());
    b = takeinput();
    c2 = b[b1-1];
    
    c = set(c1).intersection( set(c2) );
    l = len(c);
    #print c1;
    #print c2
    if(l == 1):
        print ("Case #"+str(i+1)+": "+str(c.pop()));
    elif(l > 1):
        print ("Case #"+str(i+1)+": Bad magician!");
    else:
        print ("Case #"+str(i+1)+": Volunteer cheated!");
        
sys.stdout = orig_stdout
f.close();
out.close();


    
