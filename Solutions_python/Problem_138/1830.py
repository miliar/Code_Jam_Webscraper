def main():
  print "Deceitful War Algorithm"
  print "Please enter the input file name"
  file_name = raw_input()

  with open(file_name, 'r') as f:
    with open('output.txt', 'w') as output:
      t = int(f.readline()) # Test cases

      test_case_size = 3

      for i in range(t):
        test_case = []

        for j in range(test_case_size):
          test_case.append(f.readline())

        result = solve(test_case)
        output.write("Case #" + str(i + 1) + ": " + result + "\n")

def solve(test_case):
  n = int(test_case[0])
  naomi = [float(x) for x in test_case[1].split()]
  ken   = [float(x) for x in test_case[2].split()]

  naomi.sort()
  ken.sort()

  deceitful_score = n
  normal_score    = n

  # Deceitful Score
  i = 0
  j = 0
  passed = 0
  while i + passed < n:
    if naomi[i + passed] < ken[j]:
      passed += 1
    else:
      i += 1
      j += 1

  deceitful_score -= passed
  """
  i = n / 2
  l, r = 0, n

  while(naomi[i] > ken)
  """
  # Normal score
  x = n - 1
  y = n - 1
  while y >= 0 and x >= 0:
    if ken[y] > naomi[x]:
      normal_score -= 1
      y -= 1
    x -= 1

  return str(deceitful_score) + ' ' + str(normal_score)

main()