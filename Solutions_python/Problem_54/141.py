import sys, os, copy

def gcd(nums):
   nums = copy.deepcopy(nums)
   nums.sort()
   while nums[0] == 0: nums = nums[1:]
   while len(nums) > 1:
      for i in range(1, len(nums)):
        nums[i] %= nums[0]
      nums.sort()
      while nums[0] == 0: nums = nums[1:]
   return nums[0]
   
def min(nums):
  res = nums[0]
  for i in range(len(nums)):
    if res > nums[i]:
      res = nums[i]
  return res

def algo(nums2):
  nums2.sort()
  nums = copy.deepcopy(nums2)
  nums2.reverse()
  n = len(nums)
  for i in range(1, n):
    nums[i] = nums[i] - nums[0]
  nums = nums[1:]
  g = gcd(nums)
  diff = g - nums2[0] % g
  diff = diff % g
  for i in range(len(nums2)):
    nums2[i] += diff
  while gcd(nums2) != g:
    for i in range(len(nums2)):
      nums2[i] += g
    diff += g
  return diff
  

fd = open(sys.argv[1], "r")
num = int(fd.readline())
for i in range(num):
  inp = fd.readline()
  inp = inp.split(" ")
  inp = inp[1:]
  nums = []
  for n in inp:
    nums += [int(n)]
  print "Case #%d: %s" % (i+1, algo(nums))
  