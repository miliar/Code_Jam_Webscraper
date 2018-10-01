def main():
  T = int(raw_input())
  for case in xrange(T):
    (x, r, c) = (int(x) for x in raw_input().split())
    winner = ""
    if x == 1:
      winner = "GABRIEL"
    elif x == 2:
      if r*c%2 == 0:
        winner = "GABRIEL"
      else:
        winner = "RICHARD"
    elif x == 3:
      if (r < 3 and c < 3) or (r*c%3 != 0) or (r == 1 or c == 1):
        winner = "RICHARD"
      else:
        winner = "GABRIEL"
    else:
      if (r < 4 and c < 4) or (r*c%4 != 0) or (r <= 2 or c <= 2):
        winner = "RICHARD"
      else:
        winner = "GABRIEL"
    print "Case #%d: %s" % (case+1, winner)

if __name__ == "__main__":
  main()
