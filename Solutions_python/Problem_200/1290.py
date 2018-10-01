
def solve(n):
    if n < 10:
        return n

    s = str(n)

    while True:
        if s[0] > s[1]:
            if s[0] == '1':
                return "".join(['9' for _ in range(1,len(s))])
            else:
                return "".join([chr(ord(s[0])-1)] + ['9' for _ in range(1,len(s))])

        for i in range(2, len(s)):
            if s[i] < s[i-1]:
                s = "{}{}{}".format(s[0:i-1],chr(ord(s[i-1])-1), "".join(['9' for _ in range(i, len(s))]))
                break
        else:
            return s



t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = int(input())

  print("Case #{}: {}".format(i, solve(int(n))))
  # check out .format's specification for more formatting options
