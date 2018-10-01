infile = open('B-large.in','r')
outfile = open('2out.txt','w')

total = int(infile.readline())
for t in range(total):
    line = infile.readline().split(' ')
    c = float(line[0])
    f = float(line[1])
    x = float(line[2])

    farms = [0]
    time = [0]
    time[0] = float(x/2)
    i=0
    while True:
        i+=1
        farms.append(0)
        time.append(0)
        farms[i] = farms[i-1] + float(c/(2+f*(i-1)))
        time[i] = farms[i] + float(x/(2+f*i))
        if time[i]>time[i-1]:
            break
    outfile.write('Case #'+str(t+1)+': '+str(time[i-1])+'\n')
infile.close()
outfile.close()
