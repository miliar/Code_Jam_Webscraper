def alg(grid):
    print(grid)

    wins = [0]*len(grid)
    losses = [0]*len(grid)

    owp = [0]*len(grid)
    oowp = [0]*len(grid)
    rpi = [0]*len(grid)
    
#    wins_x = [ [0]*len(grid) for i in range(len(grid)) ]
#    losses_x = [ [0]*len(grid) for i in range(len(grid)) ]

    for i in range(len(grid)):
        wins[i] = grid[i].count('1')
        losses[i] = grid[i].count('0')
        
    for me in range(len(grid)):
        sum_wp = 0
        num_opponents = 0
        for aite in range(len(grid)):
            if grid[me][aite] == '.':
                continue
            
            t_wins = wins[aite]
            t_losses = losses[aite]
            
            print(str(aite)+" "+str(t_wins)+" "+str(t_losses))
            
            if grid[me][aite] == '1':
                t_losses = t_losses - 1
            if grid[me][aite] == '0':
                t_wins = t_wins - 1
#                t_losses = t_losses - 1
            
            sum_wp = sum_wp + 1.0*t_wins/(t_wins+t_losses)
            num_opponents += 1
            
        owp[me] = sum_wp/num_opponents

    for me in range(len(grid)):
        sum_owp = 0
        num_opponents = 0
        for aite in range(len(grid)):
            if me == aite:
                continue

            if grid[me][aite] != '.':
                num_opponents += 1
                sum_owp += owp[aite]
                
        oowp[me] = 1.0*sum_owp / num_opponents

    for me in range(len(grid)):
        wp = 1.0*wins[me] / (wins[me]+losses[me])
        print("#"+str(me)+" "+str(wp)+" "+str(owp[me])+" "+str(oowp[me]))
        rpi[me] = 0.25*wp + 0.5*owp[me] + 0.25*oowp[me]
    
    return [str(i)+'\n' for i in rpi]

if __name__ == '__main__':
    fname = "A"
#    f = open(fname+".in.txt", "r")
#    f = open("/home/lawford/Desktop/"+fname+"-small-attempt0.in")
    f = open("/home/lawford/Desktop/"+fname+"-large.in")
    num_cases = int(f.readline().split(' ')[0])
    cnt=1
    fout = open(fname+".out.txt", "w")

# 1-part problem
#    piece1 = f.readline()
#    while piece1 != '':
#        result = alg(piece1.split(' ')[1:])
#        fout.write("Case #"+str(cnt)+": "+" ".join(map(str, result))+"\n")
#        piece1 = f.readline()


    for case in range(num_cases):
        grid_size_s = f.readline()
        grid_size = int(grid_size_s.split(' ')[0])
        grid = []
        for i in range(grid_size):
            grid.append(f.readline().strip())

        result = alg(grid)
            
        fout.write("Case #"+str(cnt)+": \n"+"".join(map(str, result))+"\n")
#        piece1 = f.readline()
        

# 2-part problem
#    piece1 = f.readline()
#    while piece1 != '':
#        num_lines = int(piece1)
#        lines = []
#        for i in range(0, num_lines*2-1):
##            [s,e] = map(int, f.readline().split(" "))
#            line = f.readline().strip()
#            print(line)
#            lines.append( map(int, line.split(" ")) )
#        result = alg(lines)
#        fout.write("Case #"+str(cnt)+": "+" ".join(map(str, result))+"\n")
#        piece1 = f.readline()

        cnt = cnt+1
    fout.close()
    f.close()
