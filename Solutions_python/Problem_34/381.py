#!/usr/bin/env python
import sys, re

def main():
  (L, D, N) = map(lambda x:int(x), sys.stdin.readline().split(' '))

  indices = []
  for i in range(L):
    indices.append(dict())
  lang = []
  for i in range(D):
    word = sys.stdin.readline().rstrip()
    letters = list(word)
    for j in range(len(letters)):
      if letters[j] in indices[j]:
        indices[j][letters[j]].add(i)
      else:
        indices[j][letters[j]] = set([i])
    lang.append(word)

  pattern = re.compile(r'\([a-z]+?\)|[a-z]')
  for i in range(N):
    string = sys.stdin.readline().rstrip()

    msg = pattern.findall(string)
    for j in range(L):
      if len(msg[j]) > 1:
        msg[j] = msg[j].rstrip(')').lstrip('(')

    words = set()
    for j in range(L):
      subset = set()
      for k in list(msg[j]):
        if k in indices[j]:
          subset |= indices[j][k]
      if j == 0:
        words = subset
      else:
        words &= subset
    print 'Case #' + str(i + 1) + ':', len(words)

  

if __name__ == '__main__':
  main()
