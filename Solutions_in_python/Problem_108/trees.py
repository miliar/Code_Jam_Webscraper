f=open('a.txt','r')
g=open('t.txt','w')

def getpytha(a,b):
	return float((a**2+b**2)**.5)

def merge(left, right,q):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i][q] <= right[j][q]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result+=left[i:]
    result+=right[j:]
    return result

def mergesort(list,q):
    if len(list) < 2:
        return list
    middle = len(list) / 2
    left = mergesort(list[:middle],q)
    right = mergesort(list[middle:],q)
    return merge(left, right,q)


def getmax(j,height,k):
	global vines,d,win
	loc=vines[j][0]
	if loc+height>=d:
		win=True
	if win==True:
		return 0
	maxr=0
	maxk=0
	maxh=0
	poss=[]
	if k>=len(vines): return 0
	while vines[k][0]<=loc+height:
		if vines[k][0]-loc<=vines[k][1]:
			h=vines[k][0]-loc
			reach=vines[k][0]+h	
		else:
			h=vines[k][1]
			reach=vines[k][0]+h
		poss.append([k,h,reach])
		k+=1
		if k>=len(vines): break
	poss=mergesort(poss,2)
	for z in poss:
		getmax(z[0],z[1],k)
		if win:  return 0
	return 0
	

for i in range(1,1+int(f.readline())):
	t=int(f.readline())
	vines=[]
	for j in range(t):
		x=[int(j) for j in f.readline().split()]
		vines.append(x)
	d=int(f.readline())
	loc=vines[0][0]
	height=vines[0][0]
	j=0
	k=1
	win=False
	getmax(0,height,1)
	print 'Case #' + str(i) + ':',
	g.write('Case #' + str(i) + ': ')
	if win:
		print 'YES'
		g.write('YES' + '\n')
	else:
		print 'NO'
		g.write('NO' + '\n')

g.close()
	
		
	
	