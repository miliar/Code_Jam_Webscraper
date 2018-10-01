import sys


def solve_line(line_num, line):
    result = 0

    nums = line.split(' ')
    # N = int(nums[0])
    S = int(nums[1])
    p = int(nums[2])
    nums = [int(x) for x in nums[3:]]

    num_gt_p = 0
    num_gt_p_when_surprising = 0

    for n in nums:
        largest_vote = 0
        largest_vote_requires_surprise = False
        can_go_minus_one = False

        if n == 0:
            largest_vote = n
        else:
            if (float(n) / 3) == (n / 3):
                largest_vote = (n / 3) + 1
                largest_vote_requires_surprise = True
                can_go_minus_one = True
            else:
                if int(round(float(n) / 3)) == (n / 3):
                    largest_vote = (n / 3) + 1
                else:
                    largest_vote = (n / 3) + 2
                    largest_vote_requires_surprise = True
                    can_go_minus_one = True

        if can_go_minus_one and ((largest_vote - 1) >= p):
            num_gt_p += 1
        elif largest_vote >= p:
            if largest_vote_requires_surprise:
                num_gt_p_when_surprising += 1
            else:
                num_gt_p += 1

    if num_gt_p_when_surprising > S:
        num_gt_p_when_surprising = S

    result = num_gt_p + num_gt_p_when_surprising

    return result


def process_results(results):
    with open('problem_b_solution.txt', 'w') as f:
        for i, r in enumerate(results):
            f.write('Case #%d: %s\n' % (i + 1, r))


def main():
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        lines = f.readlines()
        lines = lines[1:]

        results = []

        for i, line in enumerate(lines):
            results.append(solve_line(i + 1, line))
            process_results(results)


if __name__ == '__main__':
    main()
