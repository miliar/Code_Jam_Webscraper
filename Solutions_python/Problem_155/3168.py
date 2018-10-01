filename = "A-large.in"
f = open(filename)
incoming = f.read().split("\n")[1:-1]

for j in range(len(incoming)):
	item = incoming[j].split(" ")
	maxShyness = item[0]
	aud = [int(x) for x in list(item[1])]

	standing = 0
	friends = 0
	for i in range(len(aud)):
		if(standing >= i):
			standing += aud[i]
		else:
			friends += 1
			standing += 1 + aud[i]
	print("Case #", j+1, ": ", friends, sep="")
