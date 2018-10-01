class Digit:

    def __init__(self, digit_str, left_hand_digit=None):
        if digit_str not in set("0123456789"):
            raise ValueError("Invalid digit")
        self.value = int(digit_str)
        self.left_hand_digit = left_hand_digit

    def __eq__(self, other):
        return self.value == other

    def __repr__(self):
        return str(self.value)

    def decrement_digit(self):
        if self.value == 0:
            assert self.left_hand_digit is not None, "Cannot decrement zero"
            self.value = 9
            self.left_hand_digit.decrement_digit()
        else:
            self.value -= 1

    def set_to_next_nine_down(self):
        assert self.left_hand_digit is not None, "Cannot go below single digit"
        self.value = 9
        self.left_hand_digit.decrement_digit()


class Number:

    def __init__(self, number_string):
        self.digits = []
        current_digit = None
        for digit in number_string:
            current_digit = Digit(digit, left_hand_digit=current_digit)
            self.digits.append(current_digit)

    def __repr__(self):
        return "".join([str(d) for d in self.digits])

    def output_solution(self):
        self.set_to_previous_tidy_number()
        return str(self)

    def set_to_previous_tidy_number(self):
        self.remove_leading_zeros()
        while not self.is_tidy_number():
            self.last_non_nine().set_to_next_nine_down()
            self.remove_leading_zeros()

    def remove_leading_zeros(self):
        start = self.first_digit_without_value(self.digits, 0)
        if start is None:
            self.digits = [Digit('0')]
        self.digits = self.digits[start:]

    def is_tidy_number(self):
        highest_so_far = 0
        for digit in self.digits:
            if highest_so_far > digit.value:
                return False
            highest_so_far = digit.value
        return True

    def last_non_nine(self):
        dist_from_end = self.first_digit_without_value(reversed(self.digits), 9)
        assert dist_from_end is not None, "All digits are equal to 9"
        return self.digits[len(self.digits) - dist_from_end - 1]

    @staticmethod
    def first_digit_without_value(digits, value):
        try:
            return next(i for i, d in enumerate(digits) if not d == value)
        except StopIteration:
            return None


num_lines = int(input())
for i in range(1, num_lines + 1):
    number_str = input()
    number = Number(number_str)
    print("Case #{}: {}".format(i, number.output_solution()))
