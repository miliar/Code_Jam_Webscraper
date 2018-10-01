read_file = open('A-large.in','r')

n_cases = int(read_file.readline())

for i in range(n_cases):
    L = read_file.readline().split(" ")
    length = int(L[0])+1
    string = L[1]

    cumul = int(string[0])
    needed = 0

    for car in range(1,length):
        if cumul < car:
            needed += 1
            cumul += 1
        cumul += int(string[car])

    print("Case #"+str(i+1)+": "+str(needed))
