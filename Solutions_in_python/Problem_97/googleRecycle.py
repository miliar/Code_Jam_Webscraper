def rotate(m, A, B, rotList):    
    
    numList = [int(i) for i in str(m)]
    for i in range(len(numList)):
        a = numList.pop(0)
        numList.append(a)
        n = int(''.join(map(str, numList)))
        #print n
        if (n >= A and n < m and m <= B):
            rotList.append([n, m])

def answer(A, B):
    listt = []
    for i in range(A, B + 1):
        rotate(i, A, B, listt)
        output_list = []
        x = 0
        y = 0

        for index, item in enumerate(listt):
            x += 1
            if item not in listt[0:index]:
                y += 1
                output_list.append((x, y))
    return len(output_list)
    
read = open("/home/deepak/Desktop/C-small-attempt0.in", 'r')
write = open("/home/deepak/Desktop/output.txt", 'w')

it=int(read.readline())
for i in range(it):
    s=read.readline().split()
    A=int(s[0])
    B=int(s[1])
    x=answer(A,B)
    write.write("Case #"+str(i+1)+": "+ str(x)+"\n")
    
    
    
    
