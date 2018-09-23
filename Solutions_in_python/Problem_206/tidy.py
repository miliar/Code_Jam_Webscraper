from __future__ import division
def process (arr, t) :
  if (arr[0][1] == 1):
    print(arr[1][1] + t)
    return arr[0][0] / ((arr[0][0] - arr[1][0]) / (arr[1][1]) + t)
  if (arr[0][1] == 2):
    if (isReach(arr[1], arr[2], arr[0][0])):
      print("reach")
      t1 = 0
      if ((arr[1][1] - arr[2][1]) != 0):
        t1 = t1 + (arr[2][0] - arr[1][0]) / (arr[1][1] - arr[2][1])
      print(t1)
      return process([[arr[0][0], 1], [arr[1][0] + arr[1][1] * t1, arr[1][1]]], t1)
    else:
      return process([[arr[0][0], 1], [arr[2][0] , arr[2][1]]], 0)

def isReach (arr1, arr2, des):
  t1 = (des - arr1[0]) / arr1[1]
  t2 = (des - arr2[0]) / arr2[1]
  if (t1 > t2):
    return True
  else:
    return False
import sys
with open("input.txt") as f:
  testcase = f.readlines()
testcase = [line.rstrip('\n') for line in testcase]
arr = []
i = 1
while(i < len(testcase)):
  arr1 = []
  for j in range(int(list(testcase[i].strip().split())[1]) + 1):
    #print(int(list(testcase[i].strip().split())[1]) + 1)
    arr1.append(map(int, testcase[i].strip().split()))
    i = i + 1
  arr.append(arr1)

print("arr: ", arr)
res = []
for i in range(int(testcase[0])):
  res.append("Case #" + str(i+1) +": " + "%.6f" % process(arr[i], 0))
#print("%.6f" % process([[300, 2], [120, 60], [60, 90]], 0))
print(res)
with open("output.txt", 'w') as fout:
  for i in res:
    fout.write(i + "\n")