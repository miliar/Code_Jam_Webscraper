import sys, StringIO

class RPI(object):
    def __init__(self, lines):
        self.lines = lines

    def run(self):
        teams = len(self.lines)
        wp = []
        owp = []
        oowp = []
        rpi = []
        #los/win berechnen
        for i in range(teams):
            win = 0.0
            los = 0.0
            for j in range(teams):
                if self.lines[i][j]=="1": win += 1
                if self.lines[i][j]=="0": los += 1
            if win == 0:
                wp.append(0.0)
            else:
                wp.append(win/(los+win))
        #average wp ohne i berechnen
        for x in range(teams):
            subWp = []
            for i in range(teams):
                if self.lines[x][i]==".": continue
                win = 0.0
                los = 0.0
                #nicht das team selber
                if i==x: continue
                #alle spiele ohne team x
                for j in range(teams):
                    if j!=x:
                        if self.lines[i][j]=="1": win += 1
                        if self.lines[i][j]=="0": los += 1
                if win == 0:
                    subWp.append(0.0)
                else:
                    subWp.append(win/(los+win))
            owp.append(sum(subWp)/len(subWp))
            #print "team x:%d - subWP: %s, len: %d" % (x, subWp, len(subWp))

        #oowp
        for i in range(teams):
            wps = 0.0
            count = 0
            for j in range(teams):
                if self.lines[i][j]!=".":
                    wps += owp[j]
                    count += 1
            oowp.append(wps/count)
        #rpi berechnen
        for i in range(teams):
            rpi.append(0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i])
        #print "  wp: ", wp
        #print " OWP: ", owp
        #print "OOWP:" , oowp
        return rpi







if __name__=="__main__":
    fp = sys.stdin
    for case in range(int(fp.readline())):
        count = int(fp.readline())
        lines = []
        for i in range(count):
            lines.append(fp.readline().strip())
        game = RPI(lines)
        print "Case #%d:" % (case+1)
        for c in game.run():
            print c

