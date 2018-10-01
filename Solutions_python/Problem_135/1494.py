__author__ = 'antonkov'

input = open('input', 'r')

def read_int():
    return int(input.readline())

def read_ints():
    return [int(x) for x in input.readline().split()]

t = read_int()
for test in range(t):
    print("Case #" + str(test + 1) + ": ", end="")
    def possible_set():
        ans = read_int()
        result = []
        for i in range(4):
            x = read_ints()
            if i == ans - 1:
                result = x
        return set(result)
    a = possible_set() & possible_set()
    len(a) > 1 and print("Bad magician!")
    len(a) == 0 and print("Volunteer cheated!")
    len(a) == 1 and print(a.pop())