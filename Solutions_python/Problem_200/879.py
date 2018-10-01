def f(n):
    s = str(n)
    for i in range(len(s)):
        n1 = int(s[:i+1] + s[i]*(len(s)-i-1))
        if n1>n:
            break
    n2 = int(s[i+1:]) if i < len(s)-1 else -1
    return n - n2 - 1

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = int(input())  # read a list of integers, 2 in this case
  print("Case #{}: {}".format(i, f(n)))
  # check out .format's specification for more formatting options
