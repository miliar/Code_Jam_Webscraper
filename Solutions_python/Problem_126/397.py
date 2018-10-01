f = open('small.in')

numInputs = int(f.readline())

consonants = "bcdfghjklmnpqrstvwxyz"

def solve(word, n):
  wl = len(word)
  result = 0

  for i in range(0, wl + 1):
    for j in range(i, wl + 1):

      subWord = word[i:j]
      subLength = len(subWord)

      if subLength < n:
        continue

      # print subWord

      counter = 0

      for char in subWord:
        if char in consonants:
          counter += 1
        else:
          counter = 0

        if counter >= n:
          result += 1
          break


      

  return result


for i,line in enumerate(f):
  args = line.split(' ')
  word = args[0]
  n = int(args[1])

  ans = solve(word, n)

  print 'Case #{0}: {1}'.format(i+1, ans)


