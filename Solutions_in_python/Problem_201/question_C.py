import sys
import math


class TestCase(object):
    def __init__(self, N, K):
        self.N = N
        self.K = K

    def solve(self):
        # 0-based
        tree_depth = math.floor(math.log(self.K, 2))

        # value = N / (2^(floor(log2(K)))
        top = self.N
        bottom = pow(2, tree_depth)
        value = int(math.floor(top / bottom))

        # geometric progression sum, a1=1, q=2, n=tree_depth-1
        total_tree_diff_from_N = int(pow(2, tree_depth) - 1)
        num_values_in_row = int(pow(2, tree_depth))
        row_diff_from_N = self.N - num_values_in_row * value
        num_of_smaller_values = total_tree_diff_from_N - row_diff_from_N
        row_values = [value] * (num_values_in_row - num_of_smaller_values)
        row_values += [value - 1] * num_of_smaller_values
        row_values.sort(reverse=True)
        current_value_index = self.K - total_tree_diff_from_N - 1

        longest_strike = row_values[current_value_index]

        longest_strike_div2 = longest_strike / 2
        if longest_strike % 2 == 0:
            return longest_strike_div2, longest_strike_div2 - 1
        else:
            return longest_strike_div2, longest_strike_div2

    def __str__(self):
        return "N: {0}, K: {1}".format(self.N, self.K)


def parse(input_file_path):
    test_cases = []

    with open(input_file_path, "r") as input_file:
        test_cases_number = int(input_file.readline())
        for i in xrange(test_cases_number):
            line = input_file.readline()
            values = line.split(" ")
            test_case = TestCase(N=int(values[0]), K=int(values[1]))
            test_cases.append(test_case)

    return test_cases


def main(input_file_path):
    test_cases = parse(input_file_path)

    for i, test_case in enumerate(test_cases):
        solution = test_case.solve()
        print "Case #{0}: {1} {2}".format(i+1, solution[0], solution[1])


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
