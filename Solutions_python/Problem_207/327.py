# coding: utf8
# Copyright: MathDecision


def possible(N, R, O, Y, G, B, V):
    if (R > B + Y + O):
        return False
    elif (Y > R + B + V):
        return False
    elif (R > Y + B + G):
        return False
    elif (O > B):
        return False
    elif (G > R):
        return False
    elif (V > Y):
        return False
    return True

def minspe(r, y, b, pr, par):
    inventory = [r, y, b]
    names = ['R', 'Y', 'B']
    invnames = {'R': 0, 'Y': 1, 'B': 2}
    mx = max([inventory[i] for i in range(3) if i != invnames[par]])
    maxim = [i for i in range(3) if inventory[i] == mx and i != invnames[par]]
    if mx <= 0:
        return None
    if invnames[pr] in maxim:
       i = invnames[pr]
    else:
       i = maxim[0]
    inventory[i] -= 1
    r, y, b = inventory
    return names[i], r, y, b

def minspe0(r, y, b):
    inventory = [r, y, b]
    names = ['R', 'Y', 'B']
    mx = max(inventory)
    maxim = [i for i in range(3) if inventory[i] == mx]
    i = maxim[0]
    inventory[i] -= 1
    r, y, b = inventory
    return names[i], r, y, b

def arrange(R, Y, B):
    C, R, Y, B = minspe0(R, Y, B)
    word = C
    pr = C
    response = minspe(R, Y, B, pr, C)
    while response is not None:
        # print response
        if response is None:
            return False
        else:
            C, R, Y, B = response
        word += C
        response = minspe(R, Y, B, pr, C)
    if max(R, Y, B) > 0 or word[0] == word[-1]:
        return False
    return word


def solution(R, O, Y, G, B, V):
    if min(R - G, Y - V, B - 0) < 0:
        return 'IMPOSSIBLE'
    R -= G
    Y -= V
    B -= O
    if max(R, Y, B) == 0:
        if G > 0:
            return 'GR' * G
        if V > 0:
            return 'YV' * V
        if O > 0:
            return 'OB' * O
    word = arrange(R, Y, B)
    if not word:
        return 'IMPOSSIBLE'
    else:
        if G > 0:
            i = word.find('R')
            if i == -1:
                return 'IMPOSSIBLE'
            word = word[:i + 1] + 'GR' * G + word[i + 1:]
        if V > 0:
            i = word.find('Y')
            if i == -1:
                return 'IMPOSSIBLE'
            word = word[:i + 1] + 'VY' * V + word[i + 1:]
        if O > 0:
            i = word.find('B')
            if i == -1:
                return 'IMPOSSIBLE'
            word = word[:i + 1] + 'OV' * O + word[i + 1:]
    return word

if __name__ == '__main__':
    #
    # print arrange(4,2,2)
    # exit()


    file_number = 1
    problem_name = 'stableneighbors'
    infile = '{}{}.in'.format(problem_name, file_number)
    outfile = '{}{}.out'.format(problem_name, file_number)
    responses = []
    with open(infile, 'r') as f:
        cases = int(f.readline())
        for _ in range(cases):
            N, R, O, Y, G, B, V = map(lambda x: int(x), f.readline().split(' '))
            # print N, R, O, Y, G, B, V
            res = solution(R, O, Y, G, B, V)
            responses.append(res)

    with open(outfile, 'w') as f:
        for i, r in enumerate(responses):
            f.write('Case #{}: {}\n'.format(i + 1, r))
