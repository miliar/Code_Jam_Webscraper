import sys

infile, outfile = sys.argv[1], sys.argv[2]

f = open(infile)
contents = [line.strip() for line in f]
f.close()
count = contents[0]

games = range(1,(int(count) + 1))
o = open(outfile, "a")
for i in games:
  choice1index = (( i - 1) * 10) + 1
  choice2index = (( i - 1) * 10) + 6
  choice1 = contents[choice1index]
  choice2 = contents[choice2index]
  row1 = map(int, contents[choice1index + int(choice1)].split(' '))
  row2 = map(int, contents[choice2index + int(choice2)].split(' '))
  result = list(set(row1) & set(row2))
  resultsize = len(result)
  resultstring = ""
  if resultsize > 1:
    resultstring = "Case #{0}: Bad magician!".format(str(i))
  elif resultsize == 1:
    resultstring = "Case #{0}: {1}".format(str(i), str(result[len(result) - 1]))
  else:
    resultstring = "Case #{0}: Volunteer cheated!".format(str(i))
  o.write(resultstring)
  if i != count:
    o.write("\n")
o.close()