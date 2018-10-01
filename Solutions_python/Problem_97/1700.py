# Ben Shippee 
# FirewallXIII

# GCJ 12 C
global nums
nums = []

def findpairs(lines):
	for line in lines:
		answer = 0
		numbers = [int(n) for n in line.split()]
		min = numbers[0]
		max = numbers[1]
		if (min <= 9 and max <= 9):
			answer = 0
		elif (min == max):
			answer = 0
		else:
			i = min
			while i < max:
				num_string = str(i)
				k = i+1
				while k <=max:
					num_string2 = str(k)
					j = len(num_string2)-1
					while j >0:
						a = num_string2[:j]
						b = num_string2[j:]
						if (num_string == b+a and i < k):
							answer+= 1
							break
						j-=1
					k+= 1
				i+=1
			
		nums.append(answer)
		

cases  = []
n = int(raw_input())
i = 0
while i < n:
    new_string = raw_input()
    cases.append(new_string)
    i+= 1
findpairs(cases)
i = 0
while i < n:
	print  "Case #"+str(i+1)+": "+str(nums[i])
	i += 1