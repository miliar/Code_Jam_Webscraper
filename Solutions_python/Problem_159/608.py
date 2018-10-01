

f = open('mashroomlong.txt','w')
t = int(raw_input())
for tests in range(1, t+1):
    n = int(raw_input())
    m = [int(i) for i in raw_input().split()]
    method1 = 0
    method2 = 0
    for i in range(n-1):
        if(m[i+1]< m[i]):
            method1 += m[i]-m[i+1]
            
    rate = 0
   
    for i in range(n-1):
        if(m[i]- m[i+1] > rate):
            rate = m[i] - m[i+1]
        
    for i in range(n-1):
        if(m[i]>=rate):
            method2 += rate
        else:
            method2 += m[i]
      
    ans = "Case #"+str(tests)+": "+ str(method1) + " "+ str(method2) + "\n"
    f.write(ans)
    
f.close()