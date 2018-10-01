'''
Created on 2011-05-20

@author: jason
'''

def main():
    
    fi = open("A-small-attempt2.in","r")
    fo = open("output", "w")
    
    lines = []
    for line in fi:
        lines.append(line)
    
    lines = lines[1:]
    games = []
    for line in lines:
        vals = line.split()
        numvals = []
        for val in vals:
            numvals.append(int(val))
        games.append(numvals)
    
    count = 0
    for game in games:
        count = count + 1
        n = game[0]
        pd = game[1]
        pg = game[2]
        
        broke = True
        for d in xrange(1,n+1):
            for maybewond in xrange(0,d+1):
                if (maybewond * 100) / d == pd and (maybewond * 100) % d == 0:
                    for g in xrange(d,1001):
                        for maybewong in xrange(maybewond,g+1):
                            if (maybewong * 100) / g == pg and (maybewong * 100) % g == 0 and (d - maybewond) <= (g - maybewong):
                                #print d, maybewond, g, maybewong
                                broke = False
                                break
                        if broke == False:
                            break
                    if broke == False:
                        break
            if broke == False:
                break
            
        if broke == False:
            fo.write("Case #" + str(count) + ": Possible\n")
        else:
            fo.write("Case #" + str(count) + ": Broken\n")
        
        
if __name__ == '__main__':
    main()