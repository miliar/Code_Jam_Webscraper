# t = int(input())  # read a line with a single integer
# """ Use this for running a .in file on your pc.
file_x =  open('A-large.in', 'r').readlines()
t = int(file_x[0])
# """
output_file = open('pancake_flips2.txt', 'a')

def flip_them(s, k):
    strx = []
    number_of_minus = 0
    minus_at = 0
    number_of_turns = 0

    for i in s:
        if i == "-":
            strx.append(0)
            number_of_minus += 1
        else:
            strx.append(1)

    if number_of_minus == 0:
        return 0

    if (k == number_of_minus) & (number_of_minus == len(s)):
        return 1

    for i in range(len(strx)):
        if strx[i] == 0:
            minus_at = i
            break

    while minus_at + k <= len(s):
        index = 0

        for i in range(minus_at, minus_at + k):
            if strx[i] == 0:
                strx[i] = 1
            else:
                strx[i] = 0

        number_of_turns += 1

        for i in range(len(strx)):
            if strx[i] == 1:
                index += 1
            else:
                minus_at = i
                break

        if index == len(s):
            return number_of_turns

    return "IMPOSSIBLE"

for i in range(1, t + 1):
    # s, m = [int(s) for s in input().split(" ")]
    s, k = [(s1) for s1 in str(file_x[i]).split(" ")]
    y = flip_them(s, int(k))
    # print("Case #{}: {}".format(i, y))
    output_file.write("Case #{}: {}\n".format(i, y))

output_file.close()