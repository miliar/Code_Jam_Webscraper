import sys, os

def settle(string):
   string = string.replace("\n", "")
   n = len(string)
   s = []
   for i in range(n):
      s += [string[i]]
   i = n-1
   count = 0
   while i>0:
      if s[i] == ".":
        j = i
        while j > 0:
             s[j] = s[j-1]
             j -= 1
        s[0] = "."
        count += 1
        if count<i:
            i += 1
        else:
            count = 0
      i -= 1
   string = ""
   for a in s:
      string += a
   return string
   
def check(board, i, j, k):
    n = len(board)
    piece = board[i][j]
    if piece == ".": return ""
    h = 0
    v = 0
    d1 = 0
    d2 = 0
    for x in range(1,k):
         if j <= n-k:
            if board[i][j+x] == piece: h += 1
         if i <= n-k:
            if board[i+x][j] == piece: v += 1
         if i <= n-k and j <= n-k:
            if board[i+x][j+x] == piece: d1 += 1
         if j >= k-1 and i <= n-k:
             if board[i+x][j-x] == piece: d2 += 1
    k -= 1
    if h == k or v == k or d1 == k or d2 == k: return piece
    return ""
    
def whowin(board, k):
    winner = ""
    n = len(board)
    i = 0
    while i < n:
        j = 0
        while j < n:
            winner += check(board, i, j, k)
            j += 1
        i += 1

    if "B" in winner and "R" in winner:
        return "Both"
    elif "B" in winner:
        return "Blue"
    elif "R" in winner:
        return "Red"
    else:
        return "Neither"
   
def algo(board, k):
    n = len(board)
    for i in range(n):
       board[i] = settle(board[i])
    
    return whowin(board, k)
    
fd = open(sys.argv[1], "r")
num = int(fd.readline())
for i in range(num):
    inp = fd.readline()
    inp = inp.split(" ")
    N = int(inp[0])
    K = int(inp[1])
    board = []
    for j in range(N):
       board += [fd.readline()]
    print "Case #%d: %s" % (i+1, algo(board, K))
    