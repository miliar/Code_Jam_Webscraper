mapping={'a': 'y', ' ': ' ', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'z': 'q', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm','q': 'z'}

f=open("A-small-attempt3.in").readlines()

def go():
  i_lines = [x.strip() for x in f]
  case_count=int(i_lines[0])
  i_lines = i_lines[1:]
  assert case_count==len(i_lines)
  results=[''.join([mapping[character] for character in aline]) for aline in i_lines]
  return '\n'.join(["Case #%i: %s" % x for x in zip(range(1,len(results)+1),results)])

open('A-small-attempt3.out','w').write(go())


