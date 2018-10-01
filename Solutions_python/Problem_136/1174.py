txtFile="input.txt"
txt_file = open(txtFile);

#x=int(input())
lst=[]
for line in txt_file.readlines():
    #z=input()
    a=line.strip(" ").split()
    b=[]
    for d in range(len(a)):
        b.append(float(a.pop(0)))
    #print(b)
    lst.append(b)
x=lst.pop(0).pop()
#print(lst)


output_file = open("output.txt", "w")
case=1
for i in range(len(lst)):
    factory=lst[i][0]
    speed=lst[i][1]
    target=lst[i][2]
    rate=2
    time=0.00
    while target/rate > (factory/(rate))+ (target/(rate+speed)):
        time=time+(factory/rate)
        rate+=speed
    time=time+(target/rate)
    output_file.write("Case #")
    output_file.write(str(case))
    output_file.write(": ")
    time=round(time,7)
    output_file.write(str(time))
    #print(time)
    case+=1
    output_file.write("\n")
output_file.close()
