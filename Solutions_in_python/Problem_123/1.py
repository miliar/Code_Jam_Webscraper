T = int(raw_input())
for t in range(1, T + 1):
  A, N = map(int, raw_input().split())
  motes = map(int, raw_input().split())
  motes.sort();
  # print A
  # print motes

  curops = 0
  cur = A

  def min_ops(cur, i):
    if i == len(motes): return 0
    if cur > motes[i]:
      cur += motes[i]
      return min_ops(cur, i + 1)
    else:
      # if cur + cur - 1 > motes[i]:
      #   return min_ops(cur + cur - 1, i) + 1 # inc and do it again
      # else:
      if cur == 1:
        return min_ops(cur, i + 1) + 1
      else:
        return min(min_ops(cur, i + 1) + 1, min_ops(cur + cur - 1, i) + 1) # min(skip, inc)


  print "Case #%d: %d" % (t, min_ops(A, 0))
  
