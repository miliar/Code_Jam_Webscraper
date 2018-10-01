file1 = open("B-large.in","r")
file2 = open("output","w")
T = int(file1.readline())
C, F , X, i, time = 0, 0, 0, 1, 0
results = []
form1, form2 = [[],[],[],[]], [[],[],[],[]]
for row in file1.readlines(): 
    rate = 2.0
    time = 0
    row = row.split()
    C, F, X = float(row[0]), float(row[1]), float(row[2])
    while ((C/rate)+(X/(rate+F))) < (X/(rate)):
        time += float(C/rate)
        rate += F
    time += X/rate
    file2.write("Case #"+str(i)+": "+str(time)+"\n")        
    i += 1
    
    
