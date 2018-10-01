'''
@file main.py
@brief CodeJam problem B solution.
@author apollyon <alejandro.claro@gmail.com>
@copyright 2015 Alejandro Claro.
'''

import sys
import bisect

MULTIPLICATION_MAP = \
{ \
  '11': '1',  '1i': 'i', '1j': 'j', '1k': 'k', '12': '2',  '1I': 'I', '1J': 'J', '1K': 'K', \
  'i1': 'i',  'ii': '2', 'ij': 'k', 'ik': 'J', 'i2': 'I',  'iI': '1', 'iJ': 'K', 'iK': 'j', \
  'j1': 'j',  'ji': 'K', 'jj': '2', 'jk': 'i', 'j2': 'J',  'jI': 'k', 'jJ': '1', 'jK': 'I', \
  'k1': 'k',  'ki': 'j', 'kj': 'I', 'kk': '2', 'k2': 'K',  'kI': 'J', 'kJ': 'j', 'kK': '1', \
  '21': '2',  '2i': 'I', '2j': 'J', '2k': 'K', '22': '1',  '2I': 'i', '2J': 'j', '2K': 'k', \
  'I1': 'I',  'Ii': '1', 'Ij': 'K', 'Ik': 'j', 'I2': 'i',  'II': '2', 'IJ': 'k', 'IK': 'J', \
  'J1': 'J',  'Ji': 'k', 'Jj': '1', 'Jk': 'I', 'J2': 'j',  'JI': 'K', 'JJ': '2', 'JK': 'i', \
  'K1': 'K',  'Ki': 'J', 'Kj': 'i', 'Kk': '1', 'K2': 'k',  'KI': 'j', 'KJ': 'J', 'KK': '2', \
}

def simplify_text(text, letter):
  if text:
    q2 = text.pop()
    while text and text[-1] == letter:
      q3 = text.pop()
      q2 = MULTIPLICATION_MAP[q2 + q3]
    text.append(q2)

  return text

def compute_remainder(word):
  if word:
    q1 = word.pop()

    while word:
      q2 = word.pop()
      q1 = MULTIPLICATION_MAP[q1 + q2]

    return q1

  return '1'

def is_word(word1, word2):
  if word2 == None:
    return False

  #print word1, word2

  if word1.lower() == word2.lower():
    negatives = sum(1 for x in word2 if x.isupper())

    if negatives == 0 or negatives == 2:
      return True

  return False

def find_word(word, text, result):
  found = False
  candidate = None

  if len(result) == len(word) - 1:
    candidate = result + compute_remainder(text[:])
    found     = is_word(word, candidate)
  else:
    expected = word[len(result)]

    while text:
      q1 = text.pop()

      if q1.lower() == expected:
        text = simplify_text(text, q1)
        found, candidate = find_word(word, text[:], result + q1)
        break
      if text:
        q2 = text.pop()
        q3 = MULTIPLICATION_MAP[q1 + q2]
        text.append(q3)

  return found, candidate

def solve(text):
  quaternions  = [x for x in text]
  quaternions.reverse()

  result, word = find_word('ijk', quaternions, '')
  #print found, word

  return 'YES' if result else 'NO'

def read_next_input():
  l, x = [int(x) for x in sys.stdin.readline().strip().split()]
  text = sys.stdin.readline().strip()
  result = ''

  for i in xrange(x):
    result = result + text;

  return result

def write_solution(result):
  print 'Case #' + str(caseId) + ':',
  print result

def read_arguments():
  if len(sys.argv) > 1:
    sys.stdin  = open(sys.argv[1], 'r')

  if len(sys.argv) > 2:
    sys.stdout = open(sys.argv[2], 'w')

read_arguments()

casesCount = int(sys.stdin.readline().strip())

for caseId in xrange(1, casesCount + 1):
  result = solve(read_next_input())
  write_solution(result)
