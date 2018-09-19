import sys

fh = open(sys.argv[1])
oh = open("output.txt", "w")

tests = int(fh.readline().strip())

count = 0
rows = []
ans1 = -1
ans2 = -1
test_no = 1

for line in fh.readlines():
    if not line:
        continue
    
    count = count+1
    if count == 1:
        ans1 = int(line.strip())
    elif count == 6:
        ans2 = int(line.strip())
    elif count == 10:
        rows.append([int(i) for i in line.split(' ')])

        row1 = set(rows[ans1-1])
        row2 = set(rows[ans2+3])

        ans = row1.intersection(row2)

        if len(ans) == 0:
            oh.write("Case #%d: Volunteer cheated!\n" % (test_no))
        elif len(ans) > 1:
            oh.write("Case #%d: Bad magician!\n" % (test_no))
        else:
            oh.write("Case #%d: %s\n" % (test_no, ans.pop()))
            
        test_no += 1
        ans = 0
        count = 0
        ans1 = -1
        ans2 = -1
        rows = []
    else:
        rows.append([int(i) for i in line.split(' ')])

fh.close()
oh.close()
