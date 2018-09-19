import sys
import getopt

def playWar(n, naomi, ken):
    res = 0
    while(len(naomi) > 0):
        if len(naomi) == 1:
            res += 1 if naomi[0] > ken[0] else 0
            del naomi[0]
        else:
            chosennaomi = naomi.index(max(naomi))
            if(max(ken) < naomi[chosennaomi]):
                # naomi wins
                del ken[ken.index(min(ken))]
                del naomi[chosennaomi]
                res += 1
            else:
                # ken > naomi
                del ken[ken.index(max(ken))]
                del naomi[chosennaomi]
    return res
    
def playDeceitfulWar(n, naomi, ken):
    res = 0
    _naomi = list(naomi)
    _ken = list(ken)
    while(len(_naomi) > 0):
        if len(_naomi) == 1:
            res += 1 if _naomi[0] > _ken[0] else 0
            del _naomi[0]
        elif max(_naomi) > max(_ken):
            # play normal
            chosennaomi = _naomi.index(max(_naomi))
            #_ken = sort(_ken)
            if(max(_ken) < _naomi[chosennaomi]):
                # naomi wins
                del _ken[_ken.index(max(_ken))]
                del _naomi[chosennaomi]
                res += 1
                #print('Naomi: {0} Ken: {1}'.format(_naomi, _ken))
            else:
                # ken > naomi
                del _ken[_ken.index(max(_ken))]
                del _naomi[chosennaomi]
        else:
            # deceive ken    
            chosennaomi = _naomi.index(min(_naomi))
            chosenken = _ken.index(max(_ken))
            # ken > naomi
            del _ken[chosenken]
            del _naomi[chosennaomi]
            #print('Naomi: {0} Ken: {1}'.format(_naomi, _ken))
    return res
    
def main(argv=sys.argv):
    file = open(sys.argv[1], 'r')
    lines = int(file.readline())
    for prob in range(lines):
        numBlocks = int(file.readline())
        naomi = file.readline().split()
        naomi = [float(i) for i in naomi]
        ken = file.readline().split()
        ken = [float(i) for i in ken]
        #print('Naomi'+str(naomi))
        #print('Ken'+str(ken))
        print('Case #{0}: {1} {2}'.format(prob+1,playDeceitfulWar(numBlocks, naomi, ken),playWar(numBlocks, naomi, ken)))
        

if __name__ == "__main__":
    main()