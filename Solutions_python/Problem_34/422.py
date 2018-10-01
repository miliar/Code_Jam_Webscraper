input = open('A-large.in').readlines()
out = open('A-large.out', 'w')

L, D, N = [int(x) for x in input[0].split(" ")]

import pdb
trie = {}

for word in input[1:D + 1]:
   word = word[:-1]
   d = trie
   for c in word:
        d[c] = d.get(c, {})
        d = d[c]
import string
def count(d, guess):
  if len(guess) == 0:
    return 1
  elif guess[0].isalpha():
    return 0 if guess[0] not in d else count(d[guess[0]], guess[1:])
  else:
    x = string.find(guess,')')
    answer = 0
    for c in guess[1:x]:
        answer += 0 if c not in d else count(d[c], guess[x+1:])

    return answer
        

for i, guess in enumerate(input[D+1:]):
    print i, guess
    guess = guess[:-1]
    print >>out, "Case #%d: %d" % (i+1, count(trie, guess))
