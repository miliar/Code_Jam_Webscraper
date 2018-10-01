INPUT_FILENAME = "input.txt"
OUTPUT_FILENAME = "output.txt"
INITIAL_PRODUCTION = 2  # cookies per second


def calculate(c, f, x, y):
  t = x / (2 + y * f)
  for i in range(y):
    t += c / (2 + i * f)
  return t

def main():
  with open(INPUT_FILENAME) as input:
    with open(OUTPUT_FILENAME, 'w') as output:
      num_cases = int(input.readline())
      # Lines are ones based indexed
      for case_num in range(1, num_cases + 1):
        print("Starting case #{}".format(case_num))

        c, f, x = map(
          float, input.readline().split(' '))
        print("c {},  f {}, x {}".format(c, f, x))

        results = {}
        y = 0
        ARBITRARY_NUMBER = 10
        while (y < ARBITRARY_NUMBER or results[y - 2] >= results[y - 1]):
          results[y] = calculate(c, f, x, y)
          y += 1

        fastest_time = min(results.itervalues())
        output.write("Case #{}: {}\n".format(case_num, fastest_time))

          
if __name__ == "__main__":
  main()
