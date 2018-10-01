def multi_input():
    """Take multiple inputs."""
    case_num = int(input())  # First line, determines how many
    for __ in range(case_num):
        pancakes, k = input().split()
        yield (list(pancakes), int(k))


def main():
    test_cases = multi_input()
    flip = {'+': '-', '-': '+'}
    answers = []
    for case in test_cases:
        row = case[0]
        k = case[1]
        flips = 0
        try:
            while '-' in row:
                first_sad = row.index('-')
                assert first_sad >= 0  # No negatives
                for i in range(k):
                    row[first_sad+i] = flip[row[first_sad+i]]
                flips += 1
            answers.append(flips)
        except IndexError:
            answers.append('IMPOSSIBLE')
            continue
    for i, a in enumerate(answers):
        print('Case #{i}: {a}'.format(i=i+1, a=a))


if __name__ == '__main__':
    main()
