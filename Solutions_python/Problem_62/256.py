def process(list1, list2, n):
    count = 0
    for i in range(len(list1)):
        for j in range(i,len(list1)):
            if (list1[i]<list1[j] and list2[i]> list2[j]) or ((list1[i]>list1[j] and list2[i]< list2[j])) :
                count += 1
    fo.write("Case #" + str(n) + ": " + str(count) + "\n")

f = open("h:/A-large.in", 'r')
ncase = int(f.readline())
fo = open("h:/result.txt", 'w')

for i in range(ncase):
    n = int(f.readline())
    list1 = []
    list2 = []
    for j in range(n):
        s = f.readline().split(" ")
        a = int(s[0])
        b = int(s[1])
        list1.append(a)
        list2.append(b)
    process(list1,list2, i+1)

f.close()
fo.close()