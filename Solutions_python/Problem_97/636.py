t = input()
for testcase in range(1, t+1):
    a, b = map(int, raw_input().split())
    b1 = str(b)[0]
    total = 0
    for i in range(a, b+1):
        s = str(i)
        existed = []
        for j in [x for x in range(1, len(s)) if s[x] <= b1]:
            news = s[j:] + s[0:j]
            if news > s and int(news) <= b and not news in existed:
                total += 1
                existed.append(news)
    print "Case #" + str(testcase) + ": " + str(total)

