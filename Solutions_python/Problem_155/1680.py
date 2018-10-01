import sys

with open(sys.argv[1]) as f:
    T = int(f.readline())
    for i in range(T):
        [smax, string] = f.readline().split()
        smax = int(smax)
        raised = 0
        friends = 0
        for k, char in enumerate(string):
            if k <= raised:
                raised += int(char)
            else:
                difference = k - raised
                friends += difference
                raised += difference + int(char)
        print ("Case #"+str(i+1)+": "+str(friends))
    
