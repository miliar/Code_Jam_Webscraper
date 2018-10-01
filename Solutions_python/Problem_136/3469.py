fInput = open("B-small-attempt2.in", 'r')
fOutput = open("B-small-attempt2.out", 'w')

num_cases = int(fInput.next())

for case in range(1,num_cases+1):
    C, F, X = map(float, fInput.next().split())
    min_time = float("inf")
    for n in range(int(X)):
        time = (X+(2+n*F)*sum([C/(2+k*F) for k in range(n)]))/(2+n*F) #total time, given number of cookie farms
        if time < min_time: 
            min_time = time
        else: 
            break
            
    out_str = str(min_time)    
    fOutput.write("Case #{0}: ".format(case) + out_str + "\n")    
fInput.close()
fOutput.close()