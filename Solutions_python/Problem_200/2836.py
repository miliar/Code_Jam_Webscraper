
def tidy(n):
	arr = map(int, list(n.lstrip('0')))
	res = ""
	change = False
	for j in xrange(len(arr)):
		if j < len(arr)-1 and arr[j] > arr[j+1]:
			if arr[j] >= 10:
				res = res + "9"
			else:
				res = res + str(arr[j]-1)
			arr[j+1] = arr[j+1] + 10
			change = True
		else:
			if arr[j] >= 10:
				res = res + "9"
			else:
				res = res + str(arr[j])
	
	if change:
		return tidy(res)
	else:
		return res

if __name__=="__main__":
	t = int(raw_input())
	for i in xrange(1, t + 1):
	  n = raw_input()
	  print "Case #{}: {}".format(i, tidy(n))