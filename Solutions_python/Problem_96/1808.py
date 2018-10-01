import sys
import math
t = int(sys.stdin.readline().rstrip())
for i in range(t):
  line = sys.stdin.readline().rstrip()
  arr = line.split(' ')
  n = arr.pop(0)
  s2 = int(arr.pop(0))
  p = int(arr.pop(0))
#  print "Setup: ", n, s2, p

  both = 0
  straggler = 0
  loser = 0

  for to in arr:
    tot = int(to)
    m = int(math.ceil((tot + 1) / 3)  + 1)
#    print "----", m, tot
    best_surprise_score = 0
    best_non_surprise_score = 0
    for f in range(m, m-2, -1):
      for s in range(max(0, f-2), f+1, 1):
        t = tot - (f + s)
        if t >= 0 and abs(f - t) <=2 and abs(s-t) <= 2 and t <= 10:
          score = max(f, s, t)
#          print f, s, t, "Score:", score
          if abs(f - s) == 2 or abs(f - t) == 2 or abs(t - s) == 2:
            if score > best_surprise_score:
              best_surprise_score = score
#              print "Surprised", best_surprise_score
          else:
            if score > best_non_surprise_score:
              best_non_surprise_score = score
#              print "Nope", best_non_surprise_score
    if best_surprise_score >= p and best_non_surprise_score >= p:
      both += 1
    elif best_surprise_score >= p and best_non_surprise_score < p:
      straggler += 1
    else:
      loser += 1
#    print "Damn girl", best_non_surprise_score, " ", best_surprise_score
  op = min(straggler, s2) + both
#  print "Final", both, straggler, loser
#  print "Straggler", straggler, s2, min(straggler, s2)
  sys.stdout.write("Case #" + str(i + 1) + ": " + str(op) + "\n")
