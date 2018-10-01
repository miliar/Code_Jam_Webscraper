def play_dw(num_blocks, naomi_blocks, ken_blocks):
    naomi_points = 0
    ken_points = 0
    naomi_plays, naomi_tells = get_lie(ken_blocks, naomi_blocks)
    for index, nblock in enumerate(naomi_plays):
        optimize = []
        ntell = naomi_tells[index]
        for kblock in ken_blocks:
            optimize.append(round(kblock - ntell, 5))
        sorted = list(optimize)
        sorted.sort()
        ken_scored = False
        for value in sorted:
            if value > 0.0:
                ken_scored = True
                ken_points += 1
                ken_blocks.pop(optimize.index(value))
                break
        if ken_scored == False:
            naomi_points += 1
    return naomi_points

def get_lie(ken_blocks, naomi_blocks):
    naomi_plays = []
    naomi_tells = []
    naomi_score = 0
    for kblock in ken_blocks:
    #find lowest naomi block that can beat Ken's
        optimize = []
        for nblock in naomi_blocks:
            optimize.append(round(nblock - kblock, 5))
        sorted = list(optimize)
        sorted.sort()
        naomi_scored = False
        for value in sorted:
            if value > 0.0:
                naomi_scored = True
                last_block = naomi_blocks.pop(optimize.index(value))
                #naomi_plays.append(last_block)
                #naomi_tells.append(last_block)
                naomi_score += 1
                break
        if naomi_scored == False:
            pass
            #k_sort = list(ken_blocks)
            #k_sort.sort()
            #high = k_sort[len(k_sort) - 1]
            #low = k_sort[len(k_sort) - 2]
            n_sort = list(naomi_blocks)
            n_sort.sort()
            next_play = n_sort[0]
            #next_tell = low + ((high - low) / 2)
            naomi_plays.append(naomi_blocks.pop(naomi_blocks.index(next_play)))
            #naomi_tells.append(next_tell)
    return naomi_score

def play_w(num_blocks, naomi_blocks, ken_blocks):
    naomi_points = 0
    ken_points = 0
    for nblock in naomi_blocks:
        optimize = []
        for kblock in ken_blocks:
            optimize.append(round(kblock - nblock, 5))
        sorted = list(optimize)
        sorted.sort()
        ken_scored = False
        for value in sorted:
            if value > 0.0:
                ken_scored = True
                ken_points += 1
                ken_blocks.pop(optimize.index(value))
                break
        if ken_scored == False:
            naomi_points += 1
    return naomi_points

input = open("input.txt", "r")

cases = int(input.readline())

for case in range(cases):
    num_blocks = int(input.readline())
    naomi_blocks = map(float, input.readline().split())
    ken_blocks = map(float, input.readline().split())
    
    #dw_points = play_dw(num_blocks, list(naomi_blocks), list(ken_blocks))
    dw_points = get_lie(list(ken_blocks), list(naomi_blocks))
    w_points = play_w(num_blocks, list(naomi_blocks), list(ken_blocks))
    
    
    print "Case #%i: %i %i" % (case+1, dw_points, w_points)

input.close()