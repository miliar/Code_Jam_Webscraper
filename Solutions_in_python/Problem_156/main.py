import math

t = int(input())


def set_second_highest(second_highest):
    if len(second_highest) <= 1:
        return second_highest[0]
    else:
        return second_highest[1]


def split_stack():
    if not split_factor and current_max == 9:
        if len(diners) > 0:
            if diners[0] <= 4 or diners[0] == 6:
                count = 3
            else:
                count = math.ceil(current_max / 2)
        else:
            count = 3
    else:
        count = math.ceil(current_max / 2)

    return count


for x in range(t):
    pancakes = int(input())
    diners = sorted(list(map(int, input().split())), reverse=True)
    overall_min = max(diners)
    split_total = max(diners)
    total_count = 0

    split_factor = True
    if diners.count(9) == 1:
        split_factor = False

    '''
    We can break if our total count ever becomes 
    greater that our original max value in our 
    pancakes array
    '''
    while total_count < overall_min:
        if diners[0] <= 3:
            break
        current_max = diners.pop(0)

        ''' split our currently highest value '''
        count = split_stack()

        ''' append it to our list '''
        diners.append(current_max - count)
        diners.append(count)
        diners = sorted(diners, reverse=True)

        ''' increment appropriate values '''
        total_count += 1
        split_total = min(split_total, total_count + max(diners))


    print ('Case #{0}: {1}'.format(x + 1, split_total))