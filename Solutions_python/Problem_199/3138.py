lines = open('input2.in').read().splitlines()
test = int(lines[0].strip())
out = open('output.txt', 'w')
for t in range(test):
    s, k = lines[t+1].strip().split()
    k = int(k)
    if k > len(s) and '-' in s:
        temp = "Case #%d: IMPOSSIBLE" % (t+1)
        print temp
        out.write(temp+'\n')
        continue

    count = 0
    for i in range(0, len(s) - k + 1):
        if s[i] == '-':
            s = s[0:i] + s[i:i + k].replace('-', 't').replace('+', '-').replace('t', '+') + s[i + k:]
            count += 1

    if '-' in s:
        temp = "Case #%d: IMPOSSIBLE" % (t+1)
    else:
        temp = "Case #%d: %d" % (t+1, count)
    print temp
    out.write(temp+'\n')

out.close()
