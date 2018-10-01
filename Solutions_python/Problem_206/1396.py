file = open("input")

counter_i = 1
counter_end_i = file.readline()
num = 1



def solve(Des, Nhorse, Ndis, Nspeed):
	i = 0 
	time = 0.000000
	while (i<Nhorse):
		newtime=float(Des-Ndis[i])/Nspeed[i]
		if (newtime > time):
			time = newtime
		i = i+1
	return int(1000000*Des/time)/1000000.0


while (counter_i <= int(counter_end_i.strip())):
    num = file.readline().strip().split(' ')
    Des = int(num[0])
    Nhorse = int(num[1])
    i = 0
    Ndis = []
    Nspeed = []
    while (i<Nhorse):
    	temp = file.readline().strip().split(' ')
    	Ndis.append(int(temp[0]))
    	Nspeed.append(int(temp[1]))
    	i = i+1

    counter_i=counter_i+1
    print "%s%d%s%f"%("Case #", counter_i-1, ": ",solve(Des, Nhorse, Ndis, Nspeed))
