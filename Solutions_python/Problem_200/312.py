
data = open('B-large.in', 'r').readlines()
t = int(data[0])
answ = []

def mul(x):
	p = 0
	while x >= 10:
		p += 1
		x //= 10
	return 10 ** p

def order(dig):
	p = mul(dig)
	while p >= 10:
		x, y = (dig // p) % 10, (dig * 10 // p) % 10
		if x > y:
			dig = dig // p * p - 1
			return order(dig)
		p //= 10
	return dig

for i in range(t):
	dig = int(data[i + 1])
	answ.append(order(dig))

with open('B-large.out', 'w') as f:
    for i, o in enumerate(answ):
        f.write('Case #{}: {}\n'.format(i+1, o))
