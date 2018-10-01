file_name = 'D-large.in.in'


"""returns ken's optimal move given his blocks and what naomi claimed her move is"""
def ken_decision(naomi_block, ken_blocks):
    for block in ken_blocks:
        if block > naomi_block:
            return block #lightest block that can beat naomi's block
    return ken_blocks[0] #or waste the lightest block you can


"""returns which block naomi wants to remove, and what she will say it weights"""
def naomi_deceitful_decision(naomi_blocks, ken_blocks):

    #if there's a block that beats kens lightest block, choose it and tell ken it's infinitely heavy so that he wastes
    #his lightest block
    for block in naomi_blocks:
        if block > min(ken_blocks):
            real_move = block #lightest block that beats ken's lightest block

            #this could be easily expanded to generate a random number between the possible range
            #and to remember all previous claimed blocks
            #but that is not neccessary for the correct answer and would only increase run time
            claimed_move = .99999999

            return real_move, claimed_move

    #if you have no blocks that can beat the lightest of kens blocks, give up
    else:
        real_move = naomi_blocks[0]
        claimed_move = real_move
        return real_move, claimed_move



def play_war(naomi_blocks, ken_blocks):
    naomi_score = 0

    for naomi_move in naomi_blocks:
        ken_move = ken_decision(naomi_move, ken_blocks)

        if naomi_move > ken_move:
            naomi_score += 1

        ken_blocks.remove(ken_move)

    return naomi_score

def play_deceitful_war(naomi_blocks, ken_blocks):
    naomi_score = 0
    while naomi_blocks:
        naomi_real_move, naomi_claimed_move = naomi_deceitful_decision(naomi_blocks, ken_blocks)
        ken_move = ken_decision(naomi_claimed_move, ken_blocks)

        #print naomi_blocks, ken_blocks
        #print naomi_real_move, naomi_claimed_move, ken_move

        if naomi_real_move > ken_move:
            naomi_score += 1

        ken_blocks.remove(ken_move)
        naomi_blocks.remove(naomi_real_move)

    return naomi_score

with open(file_name, 'r') as infile:
    cases = int(infile.readline())
    for case in range(1, cases+1):

        block_number = int(infile.readline())

        naomi_blocks = sorted([float(x) for x in infile.readline().split(' ')])
        ken_blocks = sorted([float(x) for x in infile.readline().split(' ')])

        naomi_blocks_cpy = [x for x in naomi_blocks]
        ken_blocks_cpy = [x for x in ken_blocks]

        reg_score = play_war(naomi_blocks, ken_blocks)
        deceitful_score = play_deceitful_war(naomi_blocks_cpy, ken_blocks_cpy)

        print 'Case #%d: %d %d' % (case, deceitful_score, reg_score)


