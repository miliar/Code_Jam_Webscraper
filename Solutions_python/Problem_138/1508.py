f = open("D-large.in",'r')

output = open('D-large.out','w')

ncases = int(f.readline())



for T in range(0,ncases):
    nblocks = int(f.readline())
    c = f.readline()
    o = f.readline()

    #fair game
    cheaters_blocks = sorted(map(float, c.split()))
    opponents_blocks = sorted(map(float, o.split()))

    cheater_points_fair = 0

    while len(cheaters_blocks):
        cheater_selection = cheaters_blocks.pop(0)
        i = len(opponents_blocks)-1

        if cheater_selection > opponents_blocks[-1]:
            opponent_selection = opponents_blocks.pop(-1)

        else:
            i = 0
            while opponents_blocks[i] < cheater_selection:
                i += 1
            opponent_selection = opponents_blocks.pop(i)

        if cheater_selection > opponent_selection:
            cheater_points_fair += 1
    
    #unfair game
    cheaters_blocks = sorted(map(float, c.split()))
    opponents_blocks = sorted(map(float, o.split()))

    cheater_points_unfair = 0

    while len(cheaters_blocks):

        allgreater = True
        i = 0
        while allgreater and i < len(cheaters_blocks):
            if opponents_blocks[i] > cheaters_blocks[i]:
                allgreater = False
            i += 1

        if allgreater:
            cheater_points_unfair = len(cheaters_blocks)
            cheaters_blocks = []

        else:
            cheater_selection = cheaters_blocks.pop(0)
            opponent_selection = opponents_blocks.pop(-1)

    output.write("Case #"+str(T+1)+": "+str(cheater_points_unfair)+" "+str(cheater_points_fair)+"\n")


output.close()
        
    
