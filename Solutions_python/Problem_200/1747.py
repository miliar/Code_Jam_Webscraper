f = open('B-large.in')

c = int(f.readline())

result = []

def is_tidy(int_list):
    return all(b >= a for a, b in zip(int_list, int_list[1:]))

def flip(int_list):
    is_fliped = False
    fliped_ipt = int_list
    for i in range(len(fliped_ipt) - 1):
        if fliped_ipt[i] > fliped_ipt[i + 1]:
            if is_fliped:
                fliped_ipt[i + 1] = 9
            else:
                is_fliped = True
                fliped_ipt[i] -= 1
                fliped_ipt[i + 1] = 9

    if is_tidy(fliped_ipt):
        return fliped_ipt
    else:
        return flip(fliped_ipt)

for case in range(c):
    ipt = f.readline().rstrip()
    if len(ipt) == 1:
        result.append('Case #' + str(case + 1) + ': ' + str(ipt) + '\n')
        continue

    ipt = list(map(lambda x: int(x), ipt))
    fliped_ipt = flip(ipt)

    # if is_tidy(ipt):
    result.append('Case #' + str(case + 1) + ': ' + ''.join(map(str, fliped_ipt)).lstrip('0') + '\n')
    # else:

out = open('B-large.out', 'w')
for l in result:
    out.writelines(l)
