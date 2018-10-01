import string

s1 = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up aoz"
s2 = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv yeq"

dct = {}

for i in range(len(s2)):
	c = s2[i]
	if c != " " and c not in dct:
		dct[c] = s1[i]

for c in list(string.ascii_lowercase):
	if c not in dct:
		missing_key = c

for c in list(string.ascii_lowercase):
	if c not in dct.values():
		missing_value = c

dct[missing_key] = missing_value
#print dct, len(dct)

f=open("A-small-attempt0.in", "r")
f2=open("gcj_output.txt", "w")
f.readline()

i=1
for line in f:
	s2 = ""
	for c in line:
		if c in string.ascii_lowercase:
			s2 +=  dct[c] 
		elif c == " ":
			s2 += " "
	
	f2.write( "Case #"+str(i)+": "+s2+ "\n" )
	i += 1