f = open('A-small-attempt1.in', 'r')
#f = open('test.in', 'r')
#lines = f.read().splitlines()

#for line in lines:
#    print(line)

def nextline():
    return f.readline().replace('\n', '')

testcount = int(f.readline())
for i in range(testcount):
    answer1 = int(nextline())
    field1 = []
    field1.append(nextline().split(' '))
    field1.append(nextline().split(' '))
    field1.append(nextline().split(' '))
    field1.append(nextline().split(' '))
    
    candidates1 = field1[answer1 - 1]
    #print(candidates1)

    answer2 = int(nextline())
    field2 = []
    field2.append(nextline().split(' '))
    field2.append(nextline().split(' '))
    field2.append(nextline().split(' '))
    field2.append(nextline().split(' '))
    candidates2 = field2[answer2 - 1]
    #print(candidates2)
    res = set(candidates1) & set(candidates2)
    #print(res)
    if len(res) == 1:
        print("Case #%d: %s" %((i+1), res.pop()))
    elif len(res) > 0:
        print("Case #%s: Bad magician!" %(i+1))
    else:
        print("Case #%d: Volunteer cheated!" %(i+1))
 
# 3
# 2
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# 3
# 1 2 5 4
# 3 11 6 15
# 9 10 7 12
# 13 14 8 16
# 2
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# 2
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# 2
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# 3
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# 
# Case #1: 7
# Case #2: Bad magician!
# Case #3: Volunteer cheated!
