def analyze(string, pattern):
  count = [0]
  def recurse(string, pattern, count):
    if pattern == "":
      count[0] += 1
      return
    first = pattern[0]
    for i in range(0, len(string)):
      if string[i] == first:
        recurse(string[i:], pattern[1:], count)
  recurse(string, pattern, count)
  return count[0]
  
print analyze("aabb", "ab")
  
  
f = open("qual3.test", "r")
num_strings = int(f.readline())

master_string = "welcome to code jam"

strings = []
for i in range(0, num_strings):
  string = f.readline()
  strings.append(string[0:len(string)-1])
  
for i in range(0, len(strings)):
  num = str(analyze(strings[i], master_string))
  if len(num) == 1:
    num = "000" + num
  elif len(num) == 2:
    num = "00" + num
  elif len(num) == 3:
    num = "0" + num
  elif len(num) > 4:
    num = num[len(num)--4:len(num)]
  
  print "Case #" + str(i+1) + ": " + num

