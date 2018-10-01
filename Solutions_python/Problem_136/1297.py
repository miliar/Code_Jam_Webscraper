for t in range(int(input())):
    l = list(map(float,input().split(" ")))
    c = l[0]; f = l[1]; x = l[2]
    tot = 0
    r = 2
    time = 0
    if(x<=c):
    	time = x/r;
    else :
    	while(True) :
    		t1 = x/r;
    		t2 = c/r;
    		if(t1>(t2+x/(r+f))):
    			tot = 0
    			r = r+f
    			time+=t2
    		else :
    			time+=t1
    			break
    print("Case #{}: {:.7f}".format(t+1,time))
    
