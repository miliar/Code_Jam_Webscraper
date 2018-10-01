def solution(row, s):
    row_bool = make_boolean(row)
    if all(row_bool):
        return 0
    row_q = [(row_bool, 0)]
    past_rows = set([row_bool])

    while len(row_q) > 0:

        #print([(make_sting(x), f) for x, f in row_q])
        rut, n_flip = row_q.pop(0)
        for new_row in calc_new_rows(rut, s):
            if all(new_row):
                return n_flip + 1
            else:
                if new_row not in past_rows:
                    past_rows.add(new_row)
                    row_q.append((new_row, n_flip + 1))
        #print(len(past_rows), len(row_q))
    return "IMPOSSIBLE"


def calc_new_rows(rut, s):

    for start in range(0, len(rut) - s +1):
        yield flip(rut, s, start)

def make_boolean(row):
    row_bool = tuple([])

    for char in row:
        row_bool += (char == "+",)
    return row_bool

def make_sting(row):
    row_string = ""

    for side in row:
        if side:
            row_string += "+"
        else:
            row_string += "-"
    return row_string

def flip(row, size, start):
    row_list = list(row)
    for i in range(start, (start+size), 1):
        row_list[i] = not row_list[i]
    return tuple(row_list)


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
total = int(input())  # read a line with a single integer
for i in range(1, total + 1):
  s, k_s = input().split(" ")  # read a list of integers, 2 in this case
  result = solution(s, int(k_s))
  print("Case #{}: {}".format(i, result))
  # check out .format's specificatin for more formatting options