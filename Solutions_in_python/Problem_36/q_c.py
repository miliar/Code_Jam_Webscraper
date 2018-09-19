lines = open("C-large.in").read().split("\n")
#print lines

n = int(lines[0])
print n

s = "welcome to code jam"

output = []
for i, x in zip(range(1,n+1), lines[1:]):
	a = [0]* len(s)
	for j in xrange(len(x)):
		a1 = a[:]
		if x[j]=="w": a[0] = a1[0] + 1
		else:
			for k in xrange(1,len(s)):
				if x[j]==s[k]:
					a[k] += a1[k-1]
	last4digits = str(a[-1]%10000)
	last4digits = '0'*(4-len(last4digits))+last4digits
	output.append("Case #" +str(i)+": " + last4digits+"\n")

print "".join(output)
open("result.txt", "w").write("".join(output))