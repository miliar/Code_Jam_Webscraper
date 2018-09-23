



def find_tidy_number(N):
    #check len 1 
    if(len(N) == 1):
        return N
    N = list(N)
    #check if already sorted

    while(N != sorted(N)):
        for i in range(len(N) - 1):
            if (int(N[i]) > int(N[i+1])):       
                new_number = int(''.join(N[i:])) - int(''.join(N[i+1:])) - 1
                new_number = str(new_number)
                if(len(new_number) < len(N[i:])):
                    for k in range(len(N[i:]) - len(list(new_number))):
                        new_number = '0' + new_number
                
                N[i:] = list(str(new_number))
            else:
                continue
    return int(''.join(N))
        




if __name__ == "__main__":
    import sys
    file = sys.argv[1]
    try:
        file = open(file,'r')
    except IOError:
        print("Can't open file")

    T = int(file.readline().rstrip())
    for i in range(T):
        N = file.readline().rstrip()
        
        print("Case #{0}: {1}".format(i+1,find_tidy_number(N) ))
