my_file = open('Input.txt',"r")
my_file2 = open('Output.txt', "w")
N = int(my_file.readline())
for i in range(1,N+1):
    a = my_file.readline().split()
    a = [float(x) for x in a]
    C = a[0]
    F = a[1]
    X = a[2]
    rate = 2
    time = 0
    while True:
        if X/rate > X/(rate+F)+C/rate:
            time += C/rate
            rate += F
        else:
            time += X/rate
            break
    my_file2.write("Case #"+str(i)+": "+str(time)+"\n")
my_file.close()
my_file2.close()