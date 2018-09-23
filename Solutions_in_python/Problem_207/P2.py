t = int(raw_input().strip())


def get_two_length_str(x, y, time):
    base_str = x + y
    return base_str * time


def get_three_length_str(x, y, z, time):
    base_str = x + y + z
    return base_str * time


def get_new_hair_list(sit_list, sorted_hairs):
    new_sit_list = []
    for hair in sorted_hairs:
        for sit in sit_list:
            if hair == len(sit):
                new_sit_list.append(sit)
                sit_list.remove(sit)
                break
    return new_sit_list

for i in range(t):
    n, r, o, y, g, b, v = map(int , raw_input().strip().split(' '))
    hair_dict = {r: 'R', y: 'Y', b: 'B'}
    sitting_list = ['R'*r, 'Y'*y, 'B'*b]
    if n / 2 < max(r, y, b):
        print 'Case #{0}: IMPOSSIBLE'.format(i+1)
    else:
        sorted_hairs = sorted([r, y, b])
        new_sit_list = get_new_hair_list(sitting_list, sorted_hairs)
        if r == y and y == b:
            print 'Case #{0}: {1}'.format(i+1,'RBY'*r)
        elif sorted_hairs[0] == 0:
            print 'Case #{0}: {1}'.format(i+1,(new_sit_list[1][0] + new_sit_list[2][0])*sorted_hairs[1])
        else:
            first_str = get_two_length_str(new_sit_list[2][0], new_sit_list[0][0], sorted_hairs[2] - sorted_hairs[1])
            second_str = get_two_length_str(new_sit_list[2][0], new_sit_list[1][0], sorted_hairs[2] - sorted_hairs[0])
            third_str = get_three_length_str(
                new_sit_list[2][0], new_sit_list[1][0], new_sit_list[0][0],sorted_hairs[1] + sorted_hairs[0] - sorted_hairs[2])
            print 'Case #{0}: {1}'.format(i+1, first_str+second_str+third_str)


