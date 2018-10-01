
def is_tidy(num):
    prev_c = '\x00'
    for c in str(num):
        if prev_c > c:
            return False
        else:
            prev_c = c
    return True


t = int(input())
n_vals = []
for i in range(0, t):
    n_vals.append(int(input()))
i = 1

for n in n_vals:
    curr_num = n
    while not is_tidy(curr_num):
        curr_num -= 1
    print("Case #{0}: {1}".format(i, curr_num))
    i += 1
