import sys


def start():
    magic = Cookie()
    magic.parse_input()
    magic.run()
    magic.print_output()


class Base():
    def __init__(self):
        self.counter = 1
        self.input_rows = []
        self.num_tests = 0
        self.output_rows = []

    def parse_input(self):
        self.num_tests = int(input())
        for x in range(0, self.num_tests):
            line = input()
            self.input_rows.append(line)

    def run(self):
        pass

    def print_output(self):
        for row in self.output_rows:
            print("Case #%d: %s" %(self.counter, row))
            self.counter += 1


class TestCase():
    def __init__(self):
        self.cost_of_farm = 0
        self.extra_cookies_per_farm = 0
        self.winning_number = 0

    def parse_line(self, line):
        split_line = line.split(" ")
        self.cost_of_farm = float(split_line[0])
        self.extra_cookies_per_farm = float(split_line[1])
        self.winning_number = float(split_line[2])

    def calc_time(self, num_to_buy):
        speed = 2
        current_cookies = 0
        if num_to_buy == 0:
            return self.winning_number / speed
        else:
            time_spent = 0
            for farm_number in range(0,num_to_buy):
                second_until_canbuy = self.cost_of_farm / speed
                current_cookies += (speed * second_until_canbuy) - self.cost_of_farm
                speed += self.extra_cookies_per_farm
                time_spent += second_until_canbuy
            return ((self.winning_number - current_cookies) / speed) + time_spent

class Cookie(Base):

    def __init__(self):
        super().__init__()
        self.test_cases = []

    def run_case(self, test_case):

        best_case = -1 #farms
        best_time = 0

        while True:
            time = test_case.calc_time(best_case + 1)
            if time < best_time or best_case == -1:
                best_case += 1
                best_time = time
            else:
                break

        return round(best_time, 7)

    def run(self):
        for x in range(0, self.num_tests):
            new_test = TestCase()
            new_test.parse_line(self.input_rows[x])
            self.test_cases.append(new_test)

        for test_case in self.test_cases:
            self.output_rows.append(self.run_case(test_case))


if __name__ == "__main__":
    start()