def find_lowest_winner(weight_to_beat, options):
    for i, item in enumerate(options):
        if item > weight_to_beat:
            return i
    return None

f = open("D-large.in", "r+")
output = open("output.txt", "w")

num_cases = int(f.readline())

for case_num in range(0, num_cases):
    num_blocks = int(f.readline())

    naomi_blocks = [float(i) for i in f.readline().split(" ")]
    ken_blocks = [float(i) for i in f.readline().split(" ")]

    naomi_blocks.sort()
    ken_blocks.sort()

    ken_blocks_war = ken_blocks[:]

    war_wins = 0
    for block in naomi_blocks:
        ken_index = find_lowest_winner(block, ken_blocks_war)
        if ken_index == None:
            war_wins += 1
            ken_index = 0

        ken_blocks_war.pop(ken_index)

    dwar_wins = 0
    for i, block in enumerate(naomi_blocks):
        if block < ken_blocks[0]:
            ken_blocks.pop()
        else:
            dwar_wins += 1
            ken_blocks.pop(0)
    
    output.write("Case #" + str(case_num + 1) + ": " + str(dwar_wins) + " " + str(war_wins) + "\n")


f.close()
output.close()
