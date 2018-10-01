import sys

def main():
  readInput()

def readInput():
  i = sys.stdin
  o = ""
  if len(sys.argv) >= 2:
    fn = sys.argv[1]
    if fn != "-":
      i = open(fn)
      o = open(fn.replace("in", "out"), "w")

  cases = int(i.readline())
  for c in range(cases):
    o.write("Case #%i: %s\n" % (c + 1, calcSeconds(i.readline())))
  i.close()
  o.close()

def calcSeconds(line):
  line = line.split(" ")
  C = float(line[0])
  F = float(line[1])
  X = float(line[2])

  seconds = 0
  cookie = 2

  while (C / cookie + X / (cookie + F)) < (X / cookie):
    seconds += C / cookie
    cookie += F

  seconds += X / cookie

  return str(round(seconds, 7))

if __name__ == "__main__":
  main()
