file = open("input")

counter_i = 1
counter_end_i = file.readline()

def multi(a,b):
	if a=='1' and b == '1':
		return '1'
	elif a=='1' and b == 'i':
		return 'i'
	elif a=='1' and b== 'j':
		return 'j'
	elif a=='1' and b=='k':
		return 'k'
        elif a=='i' and b=='1':
                return 'i'
        elif a=='i' and b=='i':
                return '-1'
        elif a=='i' and b=='j':
                return 'k'
        elif a=='i' and b=='k':
                return '-j'
        elif a=='j' and b=='1':
                return 'j'
        elif a=='j' and b=='i':
                return '-k'
        elif a=='j' and b=='j':
                return '-1'
        elif a=='j' and b=='k':
                return 'i'
        elif a=='k' and b=='1':
                return 'k'
        elif a=='k' and b=='i':
                return 'j'
        elif a=='k' and b=='j':
                return '-i'
        elif a=='k' and b=='k':
                return '-1'
	elif a=='-1' and b == '1':
                return '-1'
        elif a=='-1' and b == 'i':
                return '-i'
        elif a=='-1' and b== 'j':
                return '-j'
        elif a=='-1' and b=='k':
                return '-k'
        elif a=='-i' and b=='1':
                return '-i'
        elif a=='-i' and b=='i':
                return '1'
        elif a=='-i' and b=='j':
                return '-k'
        elif a=='-i' and b=='k':
                return 'j'
        elif a=='-j' and b=='1':
                return '-j'
        elif a=='-j' and b=='i':
                return 'k'
        elif a=='-j' and b=='j':
                return '1'
        elif a=='-j' and b=='k':
                return '-i'
        elif a=='-k' and b=='1':
                return '-k'
        elif a=='-k' and b=='i':
                return '-j'
        elif a=='-k' and b=='j':
                return 'i'
        elif a=='-k' and b=='k':
                return '1'


def comp_string(instr):
	tmp=instr[0]
	num=1
	while(num<len(instr)):
		tmp=multi(tmp,instr[num])
		num=num+1
	return tmp


def solve(a):
	carlen=len(a)
	if (comp_string(a)!='-1'):
		return 0
	else:
		for f_pointer1 in range(1,carlen):
			if (comp_string(a[0:f_pointer1])!='i'):
				f_pointer1=f_pointer1+1
			else:
				for f_pointer2 in range(f_pointer1+1,carlen):
					if (comp_string(a[f_pointer1:f_pointer2])!='j'):
						f_pointer2=f_pointer2+1
					else:
						if (comp_string(a[f_pointer2:carlen])=='k'):
							return 1
						else:
							f_pointer2=f_pointer2+1
	return 0



while (counter_i <= int(counter_end_i.strip())):
	current_line = file.readline().strip().split(' ')
	charnum=int(current_line[0])
	repeatnum=int(current_line[1])
	current_str = file.readline().strip()
	a = []
	issame=1
	i = 0
	while (i<repeatnum):
		i2=0
		while(i2<charnum):
			if (i2>0):
				if (current_str[i2]!=current_str[i2-1]):
					issame=0
			a.append(current_str[i2])
			i2=i2+1
		i=i+1
	if (issame==1):
		print "%s%d%s%s"%("Case #",counter_i,": ","NO")
	elif (solve(a)):
		print "%s%d%s%s"%("Case #",counter_i,": ","YES")
	else:
		print "%s%d%s%s"%("Case #",counter_i,": ","NO")

	counter_i=counter_i+1
