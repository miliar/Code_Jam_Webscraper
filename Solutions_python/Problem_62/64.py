'''
Created on 2010-05-23

@author: lawford
'''
import operator

def alg(lines):
    sl = sorted(lines, key=operator.itemgetter(0),reverse=False)
    print sl
    
    cnt = 0
    for i in range(0, len(sl)):
        endA = sl[i][1]
        for j in range(i, len(sl)):
            if sl[j][1] < endA:
                cnt = cnt+1
    
    return [cnt]

if __name__ == '__main__':
    fname = "A"
#    f = open(fname+".in.txt", "r")
#    f = open("/raid/downloads/firefox/"+fname+"-small-attempt0.in")
    f = open("/raid/downloads/firefox/"+fname+"-large.in")
    f.readline()
    cnt=1
    fout = open(fname+".out.txt", "w")

    piece1 = f.readline()
    while piece1 != '':
        num_lines = int(piece1)
        lines = []
        for i in range(0, num_lines):
            [s,e] = map(int, f.readline().split(" "))
            lines.append( (s,e) )
        result = alg(lines)
        fout.write("Case #"+str(cnt)+": "+" ".join(map(str, result))+"\n")
        piece1 = f.readline()
        cnt = cnt+1
    fout.close()
    f.close()
