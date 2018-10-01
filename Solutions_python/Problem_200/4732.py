def CheckTidy(number):
	ns = str(number)
	for i in range(len(ns) - 1, 0, -1):
		if(int(ns[i]) < int(ns[i-1])):
			return False
	return True

def Modify(number):
	nm = str(number)
	nl = list(nm)
	nr = ""

	nl[len(nl)-1] = str(9)
	nl[len(nl)-2] = str(int(nl[len(nl)-2]) -1)

	for i in range(len(nm) - 1, 0, -1):
		if(int(nl[i]) < int(nl[i-1]) or int(nl[i]) == 0):
			nl[i] = str(9)
			nl[i-1] = str(int(nl[i-1]) -1)
			chain = 1
			while(int(nl[i-chain]) < 0):
				nl[i-chain] = str(9)
				nl[i-chain-1] = str(int(nl[i-chain-1]) - 1)
				chain += 1
	
	for i in range(len(nl)):
		nr += nl[i]

	return int(nr)


t = input()
t.replace(",", "")
t = int(t.split(".")[0])
if(t < 1 or t > 100):
	exit()
n = []
for i in range(t):
	n.append(input())
	n[i] = n[i].replace(",", "")
	n[i] = int(n[i].split(".")[0])
	if(n[i] < 1 or n[i] > 1000000):
		exit()

tidy = []

for i in range (len(n)):
	aux = n[i]
	while(not CheckTidy(aux)):
		aux = Modify(aux)
	print("Case #%d: %d" % (i+1, aux))