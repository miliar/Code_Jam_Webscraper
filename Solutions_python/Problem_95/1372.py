
mp = {
  'a': 'y',
  'b': 'h',
  'c': 'e',
  'd': 's',
  'e': 'o',
  'f': 'c',
  'g': 'v',
  'h': 'x',
  'i': 'd',
  'j': 'u',
  'k': 'i',
  'l': 'g',
  'm': 'l',
  'n': 'b',
  'o': 'k',
  'p': 'r',
  'q': 'z', 
  'r': 't',
  's': 'n',
  't': 'w',
  'u': 'j',
  'v': 'p',
  'w': 'f',
  'x': 'm',
  'y': 'a',
  'z': 'q',
  ' ': ' ',
}

s1 = set(mp.keys())
s2 = set(mp.values())

# 'q' ir 'z' inti 'q' ir 'z'
n = int(raw_input())
for i in range(n):
  line = raw_input()
  result = ''.join([mp.get(letter,'?') for letter in line])
  print "Case #%d: %s" % (i + 1, result)

