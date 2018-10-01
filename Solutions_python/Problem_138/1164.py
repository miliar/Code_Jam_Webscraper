__author__ = 'Javier'

lines = tuple(open('D-large.in', 'r'))

f = open('output.txt', 'w')

num_inputs = int(lines[0])


def deceitful_war(naomi_blocks, ken_blocks, num_blocks):
    naomi_points = 0

    naomi_current_blocks = naomi_blocks
    ken_current_blocks = ken_blocks

    for i in range(num_blocks):
        if ken_current_blocks[-1] < naomi_current_blocks[-1]:
            naomi_current_blocks = naomi_current_blocks[:-1]
            ken_current_blocks = ken_current_blocks[:-1]
            naomi_points += 1
        else:
            naomi_current_blocks = naomi_current_blocks[:-1]
            ken_current_blocks = ken_current_blocks[1:]
    return naomi_points

def war(naomi_blocks, ken_blocks, num_blocks):
    naomi_points = 0

    naomi_current_blocks = naomi_blocks
    ken_current_blocks = ken_blocks

    for i in range(num_blocks):
        min_block = min(filter(lambda x: x > naomi_current_blocks[0], ken_current_blocks)+ [10])
        if min_block == 10:
            naomi_points += 1
            ken_current_blocks = ken_current_blocks[:-1]
            naomi_current_blocks = naomi_current_blocks[1:]
        else:
            pos_min_block = ken_current_blocks.index(min_block)
            ken_current_blocks = ken_current_blocks[:pos_min_block] + ken_current_blocks[pos_min_block+1:]
            naomi_current_blocks = naomi_current_blocks[1:]


    return naomi_points





for i in range(num_inputs):
    num_weighs = int(lines[1+i*3])
    naomi_blocks = list(reversed(sorted(map(float, lines[2+i*3].split()))))
    ken_blocks = list(reversed(sorted(map(float, lines[3+i*3].split()))))

    deceitful_points = deceitful_war(naomi_blocks, ken_blocks, num_weighs)
    war_points = war(naomi_blocks, ken_blocks, num_weighs)

    print >> f, 'Case #%d: %d %d'%(i+1, deceitful_points, war_points)




