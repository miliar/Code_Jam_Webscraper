def check(pancake_list):
    for i in pancake_list:
        if i != '+':
            return False
    return True


def first_dash(pancake_list):
    return pancake_list.index('-')


def flip_list(pc_list, start, k):
    p_list = list(pc_list)
    if start > (len(p_list) - k):
        return 'False'
    start -= 1
    for i in range(k):
        start += 1
        if p_list[start] == '-':
            p_list[start] = '+'
        elif p_list[start] == '+':
            p_list[start] = '-'
    return p_list


def main():
    output = ''
    input_file = open('A-large.in', 'r')
    # input_file = open('sample1.in', 'r')
    T = int(input_file.readline())
    for z in range(T):
        big_list = []
        output += 'Case #' + str(z + 1) + ': '
        test_case = input_file.readline().split(' ')
        pancakes = test_case[0]
        k = int(test_case[1])
        pancakes_list = [a for a in pancakes]
        '''
        # Testing if all pancakes are happy side up
        if check(pancakes_list):
            output += str(0) + '\n'
            continue
        # Testing if sad pancakes are less than k
        sad = 0
        for a in pancakes_list:
            if a == '-':
                sad += 1
        if sad < k:
            output += 'IMPOSSIBLE\n'
            continue
        # Testing if all pancakes are blank side up
        all_sad = True
        for a in pancakes_list:
            if a != '-':
                all_sad = False
        if all_sad:
            # Testing if k is a divisor of pancakes
            if len(pancakes_list) % k == 0:
                output += str(int(len(pancakes_list) / k)) + '\n'
                continue
            else:
                # Testing if total pancakes and k are odd
                if k % 2 != 0 and len(pancakes_list) % 2 != 0:
                    output += 'IMPOSSIBLE\n'
                    continue
                # Testing if pancakes is odd and k is even
                if k % 2 == 0 and len(pancakes_list) % 2 != 0:
                    output += 'IMPOSSIBLE\n'
                    continue
        '''
        flips = 0
        repeated = False
        big_list.append(pancakes_list)
        while not check(pancakes_list):
            dash = first_dash(pancakes_list)
            new_pancake_list = flip_list(pancakes_list, dash, k)
            if new_pancake_list == 'False':
                repeated = True
                break
            flips += 1
            if new_pancake_list in big_list:
                repeated = True
                break
            big_list.append(new_pancake_list)
            pancakes_list = list(new_pancake_list)
        if repeated:
            output += 'IMPOSSIBLE\n'
            continue
        else:
            output += str(flips) + '\n'
            continue
    outp = open('A-large.out', 'w')
    outp.write(output)
    outp.close()
    # print(output)

if __name__ == '__main__':
    main()
