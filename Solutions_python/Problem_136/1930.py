Filename = 'B-small-attempt0.in'

with open(Filename,'r') as file_seq:
    all_lines = list()
    for line in file_seq.readlines():
        line = line.rstrip().split()
        x = list()
        for i in range(len(line)):
            x.append(float(line[i]))
        all_lines.append(x)

numCases = all_lines[0][0]

##cList = list()
##fList = list()
##xList = list()
##x = all_lines[1:]
##
##for i in range(len(x)):
##    cList.append(x[i][0])
##    fList.append(x[i][1])
##    xList.append(x[i][2])
tot_times = list()
y = all_lines[1:]

def cal_time(c,rate,numFarms,f):
    return c/(rate + numFarms*f) 

all_tot_times = list()

for i in range(int(numCases)):
    c,f,x = y[i][0],y[i][1],y[i][2]
    farmsTimes = list()
    tot_times = list()
    maxFarms = x/c
    rate = 2
    tot_times.append(x/rate)
    for j in range(int(maxFarms)+1):
        time = cal_time(c,rate,j,f)
        farmsTimes.append(time)
        time2 = sum(farmsTimes)
        rate2 = rate + (j+1)*f
        tot_times.append(round(time2 + x/rate2,7))
    all_tot_times.append(min(tot_times))
   

filename2 = 'B-small-attempt0-output.txt'

with open(filename2, 'w') as file_seq:
    for i in range(0,int(numCases)):
        s = 'Case #'+str(i+1)+': '+str(all_tot_times[i])+'\n'
        file_seq.writelines(s)

