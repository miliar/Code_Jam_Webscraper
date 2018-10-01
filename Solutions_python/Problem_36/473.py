import sys

text = "welcome to code jam"

n = None
i = 0
for line in sys.stdin:
  line = line.strip()
  if n == None:
    n = int(line)
    i = 0
  else:
    count = 0
    tree  = [""]
    for c in line:
      for node in tree:
        new_node = node + c
        if text[0: len(new_node)] == new_node:
          if len(new_node) == len(text):
            count += 1
          else:
            tree.append(new_node)

    result = "0000" + str(count)
    print "Case #" + str(i + 1) + ": " + result[len(result) - 4: len(result)]

    i += 1 
    if i >= n : break

