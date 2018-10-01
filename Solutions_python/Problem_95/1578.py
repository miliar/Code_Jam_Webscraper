import os

s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysizq"
s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
s4 = "our language is impossible to understandqz"
s5 = "there are twenty six factorial possibilities"
s6 = "so it is okay if you want to just give up"

table = {}
for ch1, ch4 in zip(s1, s4):
	table[ch1] = ch4
for ch2, ch5 in zip(s2, s5):
	table[ch2] = ch5
for ch3, ch6 in zip(s3, s6):
	table[ch3] = ch6

inp = open("input.txt", "r");
src = inp.readlines();
out = open("output.txt", "w");
for i in range(1, len(src)):
	res = "".join(map(lambda x: table.get(x, x), src[i]))
	out.write("Case #" + str(i) + ": " + str(res));
out.write("\n");

