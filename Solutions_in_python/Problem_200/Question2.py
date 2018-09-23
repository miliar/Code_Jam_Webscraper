def tidy(input):
    while True:
        test = list(str(input))
        for i in range(len(test)):
            if i+1 == len(test):
                return int(''.join(test))
            if int(test[i]) <= int(test[i+1]):
                continue
            else:
                break        
        input -= 1

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
	
    print('Case #%i: %i' % (i,tidy(n)))  