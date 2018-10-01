repeat = int(input())
for i in range(repeat):
    N = int(input())
    data = []
    cnt = 0
    flag = False
    for j in range(N):
        line = []
        str0 = input()
        #print(str0)
        pref = str0[0]
        char = pref
        count = 1
        for k in range(1,len(str0)):
            char = str0[k]
            if char != pref:
                line.append([pref,count])
                count = 1
            else :
                count += 1
            pref = char
        line.append([char,count])
        data.append(line)
    num = len(data[0])
    for j in range(num):
        char = data[0][j][0]
        sum = data[0][j][1]
        flag = False
        for k in range(1,N):
            if len(data[k]) != num or data[k][j][0] != char:
                flag = True
            else:
                sum += data[k][j][1]
            if flag:
                break
        if flag:
            break
        avg = 1.0*sum/N
        smaller = 0
        larger = 0
        for k in range(N):
            if data[k][j][1] < avg:
                smaller += 1
            elif data[k][j][1] > avg:
                larger +=1
        if smaller >= larger:
            avg = int(avg)
        else:
            avg = int(avg)+1
        for k in range(N):
            cnt += int(abs(avg-data[k][j][1]))
    if flag:
        print ("Case #"+str(i+1)+": Fegla Won")
    else:
        print ("Case #"+str(i+1)+": "+str(cnt))
