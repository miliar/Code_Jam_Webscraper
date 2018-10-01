with open("A-large.in") as f:
    content = f.readlines()
content = [x.strip() for x in content]
test_cases = int(content[0])
f = open("answers 1.odt","w+")
q = 1
x = 1
spead = 0
for i in range(1,test_cases+1):
    info = content[x].split(' ')
    lst = []

    for j in range(1,int(info[1])+1):
        data = content[x+j].split(" ")
        dis = int(info[0]) - int(data[0])
        time = round(float(dis / int(data[1])),6)
        lst.append(time)
    t = max(lst)
    spead = round(float(int(info[0]) / t),6)
    f.write("Case #%d: %s\r\n" % (q,spead))
    q += 1
    x += int(info[1]) +1

