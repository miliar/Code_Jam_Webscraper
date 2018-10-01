f = open('B-large.in', 'r')
g = open('output_B_large.txt', 'w')
num_loops = int(f.readline())

for testCase in range(0,num_loops):
    
    N = str(f.readline())
    tidy = str(int(N))

    if len(tidy) > 1 :

        for j in range(0,len(tidy)-1):
            
            for i in range(0,len(tidy)-1):

                if tidy[i] > tidy[i+1]:
                    if i == 0:
                        tidy = str(int(tidy[0])-1) + str((10**(len(tidy)-1))-1)

                    else:
                        tidy = tidy[0:i] + str(int(tidy[i])-1) + str((10**(len(tidy)-i-1))-1)
            
                    
    string = str('Case #' + str(testCase+1) + ': ' + str(int(tidy)) + '\n')
    g.write(string)
f.close()
g.close()
