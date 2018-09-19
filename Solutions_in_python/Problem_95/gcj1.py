import string

f = open("A-small-attempt2.in", "r+")
lines = f.readlines()
#print lines[0]
num = 0
num = int(lines[0])
f = open("gcj0.txt", "w")
f.write("")
f.close()
for n in range(1, num+1):
    s=str(lines[n])
    s=s.translate(string.maketrans("emysljcpqkxvdnrabgiotuwhfz", "olanguerzimpsbtyhvdkwjfxcq"))
    f = open("gcj0.txt", "a")
    f.write("Case #%d: " % n)
    f.write(s)
    f.close()
