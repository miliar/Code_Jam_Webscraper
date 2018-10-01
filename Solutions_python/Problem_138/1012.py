import copy

def war(naomi_blocks, ken_blocks, N):
    naomi_wins = 0
    turn_count = 0
    while turn_count < N:
        ChosenNaomi = naomi_blocks[turn_count]
        KenOption = [block for block in ken_blocks if block >= ChosenNaomi]
        if KenOption == []:
            ChosenKen = ken_blocks.pop(ken_blocks.index(min(ken_blocks)))
        else:
            ChosenKen = ken_blocks.pop(ken_blocks.index(min(KenOption)))
        if ChosenNaomi > ChosenKen:
            naomi_wins += 1
        turn_count += 1    
    return naomi_wins
    
def deceitfulwar(naomi_blocks, ken_blocks, N):
    naomi_wins = 0
    turn_count = 0
    while turn_count < N:       
        ChosenNaomi = naomi_blocks[0]
        KenOption = [block for block in ken_blocks if block >= ChosenNaomi]
        if KenOption == []:
            ChosenKen = ken_blocks.pop(ken_blocks.index(min(ken_blocks)))
        else:
            ChosenKen = ken_blocks.pop(ken_blocks.index(min(KenOption)))            
        NaomiOption = [block for block in naomi_blocks if block >= ChosenKen]
        if NaomiOption != []:
            ChosenNaomi = naomi_blocks.pop(naomi_blocks.index(min(NaomiOption)))            
        if ChosenNaomi > ChosenKen:
            naomi_wins += 1
        turn_count += 1
    return naomi_wins

def gameon(f):
    T = int(f.readline())
    testcase = 0
    while testcase < T:
        N = int(f.readline()) # The number of blocks each plyyers has
        naomi_blocks_war = f.readline().split() # the masses of Naomi's blocks
        ken_blocks_war = f.readline().split() # Ken's blocks        
        naomi_blocks_dwar, ken_blocks_dwar = copy.deepcopy(naomi_blocks_war), copy.deepcopy(ken_blocks_war)
        if N == 1:
            if naomi_blocks_war[0] > ken_blocks_war[0]:
                dwarwins, warwins = 1, 1
            else:
                dwarwins, warwins = 0, 0
        else:
            dwarwins = deceitfulwar(naomi_blocks_dwar, ken_blocks_dwar, N)
            warwins = war(naomi_blocks_war, ken_blocks_war, N)
        result = "Case #" + str(testcase+1) + ": " + str(dwarwins) + " " + str(warwins)
        
        output = open('large_df_output','a')
        output.write(result+"\n")
        output.close
        
        testcase += 1

f = open('D-large.in')
gameon(f)