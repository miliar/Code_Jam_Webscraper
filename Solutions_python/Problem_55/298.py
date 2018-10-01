def get_queue(k,n,queue, dic):
	temp = 0
	string = str(queue)
	for j in range(0,n):
		if temp + queue[j]> k:
			helper = queue[j:] + queue[:j]
			dic.update({string:(temp,helper)})
			return (temp, helper, dic)
		else:
			temp += queue[j]
	dic.update({string:(temp, queue)})
	return (temp, queue, dic)
			


def solve(r,k,n,queue):
	dic = {}
	ans = 0
	for i in range(0, r):
		temp = 0
		string = str(queue)
		if dic.has_key(string):
			(temp, queue) = dic.get(string)
		else:
			(temp, queue, dic) = get_queue(k,n,queue,dic)
		ans += temp
	return ans

if __name__ == "__main__":
	f = open("c:\input.txt", "r")
	num = int(f.readline().strip())
	for i in range(1,num+1):
		(r,k,n) = map(int,f.readline().strip().split(" "))
		queue = map(int,f.readline().strip().split(" "))
		temp = solve(int(r),int(k), int(n), queue)
		print "Case #%d: %s" %(i,temp)