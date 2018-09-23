with open("A-large.in") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
f = open("answers 1.odt","w+")
for i in range(1,len(content)):
    a = list(content[i].split(" "))
    k = int(a[1])
    word = list(a[0])
    count = 0
    imp = 0
    q = i
    for j in range((len(word) +1) - k):
        if word[j] == "-":
            for c in range(j,(j+k)):
                if word[c] == "-":
                    word[c] = "+"
                else:
                    word[c] = "-"
            count += 1
    for m in range(k):
        if word[-m] == "-":
            imp = 1
    if imp == 0:
        f.write("Case #%d: %d\r\n" %(q,count))
    else:
        f.write("Case #%d: IMPOSSIBLE\r\n" % q)
f.close()
