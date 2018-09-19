
import copy

def ken_select(blocks, n_block, perceived_value):
    for index, block in enumerate(blocks):
        if block > perceived_value:
            return blocks.pop(index)
    return blocks.pop(0)


    
def naomi_select(blocks, ken_blocks):
    for index, block in enumerate(blocks):
        if block < ken_blocks[0]:
            temp = blocks.pop(index)
            return temp, ken_blocks[-1] - 0.0001
    temp = blocks.pop(0)
    return temp, ken_blocks[-1] + 0.0001
    
'''
    for x in range(0, len(blocks)):
        if blocks[x] > ken_blocks[x]:
            temp = blocks.pop(x)
            return temp, ken_blocks[-1] + 0.00111
    for index, block in enumerate(blocks):
        for ken_block in ken_blocks[::-1]:
            if block < ken_block:
                return blocks.pop(index), ken_block - 0.001
    temp = blocks.pop(0), 
    return temp, temp
'''

def naomi_bore_war(n_blocks):
    return n_blocks.pop(-1)


def victory(a, b):
    if b > a:
        return 'Naomi'
    else:
        return 'Ken'

def play_d_war(n_blocks, ken_blocks, n_points):
    block_counter = len(n_blocks)
    while block_counter != 0:
        nao, value = naomi_select(n_blocks, ken_blocks)
        winner = victory(ken_select(ken_blocks, nao, value), nao)
        if winner == 'Naomi':
            n_points += 1
        block_counter = block_counter - 1
    return n_points

def play_bore_war(n_blocks, ken_blocks, n_points):
    block_counter = len(n_blocks)
    while block_counter != 0:
        nao = naomi_bore_war(n_blocks)
        winner = victory(ken_select(ken_blocks, nao, nao), nao)
        if winner == 'Naomi':
            n_points += 1
        block_counter = block_counter - 1
    return n_points
    
    
def game_on():
    games = int(raw_input(''))
    for x in range(0, games):
        trash_variable = raw_input()
        n_blocks = map(float, raw_input().rstrip().split(' '))
        k_blocks = map(float, raw_input().rstrip().split(' '))
        n_points = 0
        n_blocks.sort()
        k_blocks.sort()

        saved_blocks = (copy.copy(n_blocks), copy.copy(k_blocks))
        game_1 = play_bore_war(n_blocks, k_blocks, n_points)
        n_points = 0
        (n_blocks, k_blocks) = saved_blocks
        game_2 = play_d_war(n_blocks, k_blocks, n_points)
        print "Case #{}: {} {}".format(x+1, game_2, game_1)


if __name__ == '__main__':
    game_on()