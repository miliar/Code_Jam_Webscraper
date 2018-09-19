f = open('B-large.in','r')
testcases = int(f.readline())
for testcase in range(1,testcases+1):
     curr_case = f.readline().split()
     C = float(curr_case[0])
     F = float(curr_case[1])
     X = float(curr_case[2])
     rate = 2.0
     seconds = 0
     while X/rate > X/(rate+F) + C/rate:
         seconds += C/rate
         rate += F
     seconds += X/rate
     output = "Case #"+str(testcase)+": "+str(seconds)
     f2 = open('B-small-out.txt',"a")
     f2.write(output)
     f2.write("\n")
     f2.close()
