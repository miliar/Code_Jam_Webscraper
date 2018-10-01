def search(eng,ql,ind):
	i = 0
	for i in range(ind,len(ql)):
		if eng == ql[i]:
			return i
	return i
