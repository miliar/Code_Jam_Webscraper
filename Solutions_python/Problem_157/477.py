dfa = {
  '1': {'i': 'i',  'j': 'j', 'k': 'k'},
  '-1': {'i': '-i',  'j': '-j', 'k': '-k'},
  'i': {'i': '-1', 'j': 'k', 'k': '-j'},
  '-i': {'i': '1', 'j': '-k', 'k': 'j'},
  'j': {'i': '-k', 'j': '-1', 'k': 'i'},
  '-j': {'i': 'k', 'j': '1', 'k': '-i'},
  'k': {'i': 'j', 'j': '-i', 'k': '-1'},
  '-k': {'i': '-j', 'j': 'i', 'k': '1'}
}

def test(string):
  state = '1'
  first, second = False, False
  for c in string:
    state = dfa[state][c]
    # first: ex. a prefix ~= "i"?
    # second: AND ex. a larger prefix ~= "k" ~= "ij"?
    first, second = first or (state == 'i'), second or (first and (state == 'k'))
  # finally: AND is the entire string equivalent to "ijk" ~= "-1"?
  # It is easily seen that if ABC ~= "ijk" AND AB ~= "ij", then C ~= k.
  return first and second and state == '-1'

def test_lazy(string, reps):
  # The string is equivalent to a single character, each of which has a maximum cycle of four.
  # After four repetitions, the DFA has started a repetition in every available state.
  # Therefore, the "i" and "ij" prefixes WILL be in the first 8 repetitions of the string if at all.
  # (8, because we need four repetitions for *each* prefix. Savvy?)
  actual_reps = min(8, reps)-1

  state = '1'
  first, second = False, False

  # Do the first rep manually, to find the final state.
  for c in string:
    state = dfa[state][c]
    # first: ex. a prefix ~= "i"?
    # second: AND ex. a larger prefix ~= "k" ~= "ij"?
    first, second = first or (state == 'i'), second or (first and (state == 'k'))

  # Calculate if the whole string will have a final state of -1.
  # 1 will never cycle through -1.
  if state == '1':
    return False

  # -1 must be repeated an odd number of times.
  if state == '-1' and (reps % 2 == 0):
    return False

  # i, j, k, -i, -j, -k must be repeated 4x+2 times.
  if state in ('i', 'j', 'k', '-i', '-j', '-k') and (reps % 4 != 2):
    return False

  # If the total checksum is correct, but the prefixes have not been found,
  # look for them in the next seven reps:
  for c in string*actual_reps:
    if first and second:
      break
    state = dfa[state][c]
    # first: ex. a prefix ~= "i"?
    # second: AND ex. a larger prefix ~= "k" ~= "ij"?
    first, second = first or (state == 'i'), second or (first and (state == 'k'))

  return first and second

def main():
  cases = int(input())
  for i in range(1, cases+1):
    l, x = map(int, input().split())
    string = input()
    print('Case #{}: {}'.format(i, ['NO', 'YES'][test_lazy(string, x)]))

def main_slow():
  cases = int(input())
  for i in range(1, cases+1):
    l, x = map(int, input().split())
    string = input()
    print('Case #{}: {}'.format(i, ['NO', 'YES'][test(string*x)]))

main()
