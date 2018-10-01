#python32
#coding = utf-8

a = list("abcdefghijklmnopqrstuvwxyz")
b = list("abcdefghijklmnopqrstuvwxyz")
d = {' ':' ','\n':'\n'}

def map(x,y):
	xs = list(x)
	ys = list(y)

	for j in range(len(xs)):
		if not xs[j] in d:
			d[xs[j]] = ys[j]
			a.remove(xs[j])
			b.remove(ys[j])
		else:
			if not d[xs[j]] == ys[j]:
				print("error")
				
map("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand")
map("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities")
map("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up")
map("a","y")
map("o","e")
map("z","q")

print(d)

if len(a) == 1:
	d[a[0]] = b[0]
	a.remove(a[0])
	b.remove(b[0])


file0 = open("A-small-attempt0.in",'r')
file1 = open("Aout","w")
num = int(file0.readline())


def trans(a):
	a0 = list(a)
	b = []
	for i in a0:
		b.append(d[i])
	return ''.join(b)

for i in range(num):
	file1.write("Case #"+str(i+1)+": "+trans(file0.readline()))
