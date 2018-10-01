def flips(s, k):
    if len(s) < k:
        for pancake in s:
            if pancake=="-":
                return "IMPOSSIBLE"
        return 0
    else:
        if s[0]=="-":
            a = ""
            for i in range(k):
                if s[i]=="-":
                    a += "+"
                else:
                    a += "-"
            new = a + s[k:]
            subresult = flips(new, k)
            if subresult=="IMPOSSIBLE":
                return "IMPOSSIBLE"
            else:
                return subresult+1
        else:
            subresult = flips(s[1:], k)
            if subresult=="IMPOSSIBLE":
                return "IMPOSSIBLE"
            else:
                return subresult

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  s, k = input().split(" ")
  print("Case #{}: {}".format(i, flips(s, int(k))))
