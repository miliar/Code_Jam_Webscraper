import sys
from multiprocessing import Pool

def solve(sentences):
  words = set()
  for s in sentences:
    for w in s:
      words.add(w)
  min_res = len(words)

  set1_e = set()
  set1_f = set()
  for w in sentences[0]:
    set1_e.add(w)
  for w in sentences[1]:
    set1_f.add(w)


  for i in range(2**(len(sentences)-2)):
    set_e = set()
    set_f = set()
    for j in range(len(sentences)-2):
      eng = (i & (2**j)) != 0
      set_x = set_e if eng else set_f
      for w in sentences[2+j]:
        set_x.add(w)
    mres = len((set_e | set1_e) & (set_f | set1_f))
    if mres < min_res: min_res = mres
  return min_res

if __name__ == '__main__':
  T = int(input())

  inputs = []

  for iCase in range(T):
    N = int(input())
    sentences = []
    for iw in range(N):
      sentences.append(input().split(' '))
    inputs.append(sentences)

  p = Pool(12)

  res = p.map(solve, inputs, 1)
  for iCase, r in enumerate(res):
    print('Case #{0}: {1}'.format(iCase+1, r))
