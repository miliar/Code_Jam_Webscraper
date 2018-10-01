def solve(problem):
    # TODO: is tidy?
    # TODO: get a real life
    tmp_string = str(problem)
    prev_letter = "0"
    for letter in tmp_string:
        if prev_letter <= letter:
            prev_letter = letter
        else:
            return 1
    return 0


def open_file(f):
    with open(f, "r") as fin:
        return fin.read().splitlines()


myArr = open_file("binput.txt")
myArr = list(map(int, myArr))

for i in range(1, myArr[0] + 1 ):
    user_in = myArr[i]
    while solve(user_in):
        user_in -= 1
    print("Case #{}: {}".format(i, user_in))