def outcome(L1, L2):
    count = 0
    var = 0
    for i in range(0,4):
        if L1[i] in L2:
            var = L1[i]
            count = count+1
    if count == 1:
        return str(var);
    elif count > 1:
        return "Bad magician!";
    elif count == 0:
        return "Volunteer cheated!";
T = int(raw_input())
B = open('GCJ2k14A1.txt','w')
for i in range(1, T+1):
    L1 = []
    L2 = []
    r1 = int(raw_input())-1
    for k in range(0,4):
        L1.append(raw_input().split(' '))
    r2 = int(raw_input())-1
    for k in range(0,4):
        L2.append(raw_input().split(' '))
    B.write("Case #" + str(i) + ': ' + outcome(L1[r1], L2[r2]) + '\n')
B.close()
