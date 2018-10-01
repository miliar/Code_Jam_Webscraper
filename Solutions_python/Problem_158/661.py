import unittest

input_file = open('D-small-attempt0.in', 'r')
number_of_tests = input_file.readline()

result_file = open("D-small-attempt0.out", "w")


def get_x_r_c(line):
    return int(line.split()[0]), int(line.split()[1]), int(line.split()[2])


def who_wins(x, r, c):
    if x == 1:
        return "GABRIEL"
    if x == 2:
        if (r * c) % 2 == 0:
            return "GABRIEL"
    if x == 3:
        if (r * c) % 3 == 0 and r > 1 and c > 1:
            return "GABRIEL"
    if x == 4:
        if (r == 4 and c == 4) or (r == 4 and c == 3) or (r == 3 and c == 4):
            return "GABRIEL"

    return "RICHARD"


for j in range(int(number_of_tests)):
    x, r, c = get_x_r_c(input_file.readline())

    print "Case #{}: {}\n".format(j + 1, who_wins(x, r, c))
    result_file.write("Case #{}: {}\n".format(j + 1, who_wins(x, r, c)))

input_file.close()
result_file.close()


class MyTestCase(unittest.TestCase):

    def test_calculate_guest_to_add(self):
        self.assertEqual(who_wins(2, 2, 2), "GABRIEL")
        self.assertEqual(who_wins(2, 1, 3), "RICHARD")
        self.assertEqual(who_wins(4, 4, 1), "RICHARD")
        self.assertEqual(who_wins(3, 2, 3), "GABRIEL")

if __name__ == '__main__':
    unittest.main()
