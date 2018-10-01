def tidy(a):
	for i in range(len(a)-1):
		if int(a[i]) > int(a[i+1]):
			return False
	
	return True

num_ip = int(raw_input())
result =[]
for i in range(num_ip):
	ip = int(raw_input())
	k = 1
	l=-2
	ips = str(ip)
	while tidy(str(ip))==False:
		ips = str(ip)
		if ips[l:]=="9"*(l*-1):
			k = k * 10
			ip = ip - k
			l = l - 1
		else:
			ip = ip - k

	result.append(ip)

j=1
for i in result:
        print "Case #{}: {} ".format(j,i)
	j = j+1



