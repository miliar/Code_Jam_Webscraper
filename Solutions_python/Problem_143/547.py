def main():
  testcases = int(input())
  for caseNr in range(1, testcases+1):
    a,b,k = map(int, input().split())
    print("Case #%i: %i" % (caseNr, solve(a,b,k)))

def solve(a,b,k):
  c = 0
  for i in range(a):
    for j in range(b):
      if i & j < k:
        c += 1
  return c


if __name__ == "__main__":
  main()
