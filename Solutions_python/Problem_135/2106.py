with open('A-small-attempt0.in') as f:
  with open('a_small_output.txt', 'w') as out:

    # Get number of test cases
    cases = int(f.readline())

    # Iterate over each test case
    for i in range(1,cases+1):
      # Get number of lines in each test case
      first_row = int(f.readline()[0])
      rows = [f.readline() for _ in range(4)]
      first_nums = rows[first_row-1].strip('\n').split(' ')
      first_nums = [int(num) for num in first_nums]

      second_row = int(f.readline()[0])
      rows = [f.readline() for _ in range(4)]
      second_nums = rows[second_row-1].strip('\n').split(' ')
      second_nums = [int(num) for num in second_nums]

      card = set(first_nums).intersection(second_nums)
      length = len(card)
      if length > 1:
        result = 'Case #' + str(i) + ': Bad magician!'
      elif length == 1:
        result = 'Case #' + str(i) + ': ' + str(card.pop())
      else:
        result = 'Case #' + str(i) + ': Volunteer cheated!'

      # Output proper result
      out.write(result)
      if i < cases:
        out.write('\n')