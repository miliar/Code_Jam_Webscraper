f = open("A-large.in", "r").read()

new_file = open("standingOvationSolLarge", "w")
splitted_file = f.split("\n")[:]
t = int(splitted_file[0])

# 
def amount_friends (n,numbers):
	friends = 0
	counter = 0
	for i in range(0,n+1):
		amount_people = numbers[i]

		if counter < i:
			friends += (i-counter)
			counter += i-counter
		counter += amount_people
		#print counter
	return friends

for i in range(1,t+1):
	n, numbers = [x for x in splitted_file[i].split(" ")]
	n = int(n)
	numbers = [int(x) for x in list(numbers)]
	new_file.write("Case #"+str(i)+ ": "+str(amount_friends(n,numbers))+"\n")

