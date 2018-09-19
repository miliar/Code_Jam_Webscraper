f = open('test.txt','r')
testcases = int(f.readline())
for testcase in range(1,testcases+1):
    count = 0
    curr_case = f.readline().split()
    A = int(curr_case[0])
    B = int(curr_case[1])
    K = int(curr_case[2])
    for k in range(0,K):
        for a in range(0,A):
            for b in range(0,B):
                if a&b == k:
                    count += 1
    output = "Case #"+str(testcase)+": "+str(count)
    f2 = open('B-small-out.txt', "a")
    f2.write(output)
    f2.write("\n")
    f2.close()
