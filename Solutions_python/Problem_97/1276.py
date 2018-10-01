def do(filename):
  ifile = open(filename, "rt")
  lines = ifile.readlines()
  ifile.close()
  ofile = open("output.txt", "wt")
  for i in range(1, len(lines)):
    ofile.write("Case #" + str(i) + ": ")
    line = lines[i]
    a = int(line[:line.find(" ")])
    b = int(line[line.find(" ") + 1:])
    res = recycled(a, b)
    ofile.write(str(res) + "\n")
  ofile.close()

def recycled(a, b):
  count = 0
  numDigits = 1
  cur = a
  while cur >= 10:
    cur /= 10
    numDigits += 1
  
  found = {}
  for n in range(a, b):
    m = n
    for perm in range(numDigits - 1):
      m = (m % 10) * (10 ** (numDigits - 1)) + m / 10
      if a <= n and n < m and m <= b:
        if found.get(n) != m and found.get(m) != n:
          count += 1
          found[n] = m
  
  return count
