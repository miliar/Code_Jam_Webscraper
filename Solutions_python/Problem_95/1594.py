import sys

dic = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
res = ""

with open(sys.argv[1], 'r') as fin:

    line = fin.readline()
    linenum = int(line.strip())
 
    for i in range(linenum):
      resl = ""
      line = fin.readline()
    
      for j in range(len(line)):
        if line[j] in dic:
          resl += dic[line[j]]
        else:
          resl += line[j]

      res += "Case #"+str(i+1)+": "+resl

with open("out.txt", 'w') as fout:
  fout.write(res)

