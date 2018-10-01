mem = dict()

def palinAndSquare(x):
  xrev = str(x)[::-1]
  check1 = str(x) == str(xrev)
  root = 1/2.0
  square = abs(x) ** root
  check2 = abs(square - int(square)) < 0.0000001
  squarecheck = int(square)
  squarerev = str(squarecheck)[::-1]
  check3 = str(squarecheck)== (squarerev)
  return check1 and check2 and check3
def check(x,y):
  final = 0
  for i in xrange(x,y+1, 1):
    if i in mem:
      final += mem[i]
    else:
      result = palinAndSquare(i)
      mem[i] = result
      final += result

  return final

def main(input1):
  out = ""
  lines = input1.split("\n")
  objects = int(lines[0])
  for i in xrange(objects):
    line = i + 1
    (x,y) = lines[line].split(" ")[0], lines[line].split(" ")[1]
    out += "Case #" + str(line) + ": " + str(check(int(x),int(y))) + "\n"
  out = out[:len(out)-1]
  print out

stuff = """100
579 817
1 121
1 654
368 482
1 484
3 65
7 121
114 886
1 302
7 122
4 104
3 122
1 1000
65 484
9 302
1 584
55 614
7 221
517 931
243 600
333 778
171 556
1 109
308 760
723 804
237 277
21 584
273 932
3 9
252 484
287 787
735 801
21 485
7 10
500 818
1 6
3 5
8 221
334 492
120 484
3 742
120 742
122 1000
121 742
7 109
1 65
554 792
464 796
229 552
7 485
8 485
4 5
21 221
1 9
120 302
564 967
122 483
8 584
121 484
865 897
1 4
168 769
3 484
3 584
1 2
1 122
65 122
1 5
288 832
303 485
8 9
8 121
79 775
44 821
10 120
7 584
9 109
384 485
406 755
623 716
484 484
307 686
21 122
9 9
3 10
484 742
100 1000
484 485
3 109
21 484
121 121
1 101
1 742
1 221
541 640
1 485
9 122
410 889
9 221
1 104
"""

main(stuff)
