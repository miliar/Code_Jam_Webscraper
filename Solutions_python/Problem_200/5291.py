import fileinput
import sys
f = fileinput.input(files='B-small-attempt1.in', mode='r')
sys.stdout = open('B-small-attempt1.out', 'w')

tc = int(f.readline())
for i in range(1, tc+1):
    num = int(f.readline().strip())
    for j in range(num, 0, -1):
        mynum = str(j)
        list = []
        if len(mynum) < 2:
            ans = mynum;
            break
        else:
            for ch in mynum:
                list.append(ch)
            flag = 0
            for k in range(0, len(list)-1):
                if len(list) < 2:
                    ans = str(mynum)
                else:
                    if list[k] <= list[k+1]:
                        flag = 0
                    else:
                        flag = 1
                        break
            if flag == 0:
                ans = str(mynum)
                break
    print("Case #" + str(i) + ": " + ans)
