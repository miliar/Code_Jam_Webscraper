import sys

for j in range(int(sys.stdin.readline())):
    n, line = sys.stdin.readline().strip().split()
    missing = 0
    standing = 0
    for k in range(len(line)):
        #print(k, standing, missing, line[k])
        if line[k] != "0":
            if standing >= k:
                standing += int(line[k])
            else:
                #print("not enough standing", k, standing, line[k])
                missing += k - standing
                standing = k + int(line[k])



    print("Case #"+str(j+1) + ": " + str(missing))
