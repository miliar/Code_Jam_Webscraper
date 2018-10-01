
def war(naomi, ken):
    na = naomi[:]
    ke = ken[:]
    score = 0
    for i in na:
        if i > ke[-1]:
            ke.pop()
            score += 1
        else:
            for j in range(len(ke)):
                if ke[j] > i:
                    ke.pop(j)
                    break
    return score

def dwar(naomi, ken):
    na = naomi[:]
    ke = ken[:]
    score = 0
    for i in ke:
        if i > na[-1]:
            na.pop()
        else:
            for j in range(len(na)):
                if na[j] > i:
                    na.pop(j)
                    score += 1
                    break
    return score


if __name__ == "__main__":
    fin = open('D-large.in', 'rb')
    input = fin.read().split('\n')
    t = int(input[0])
    fout = open('output4.txt','w')
    for i in range(t):
        baseline = i*3+1
        num = int(input[baseline])
        naomi = [float(j) for j in input[baseline+1].split(" ")]
        ken = [float(j) for j in input[baseline+2].split(" ")]
        naomi.sort()
        ken.sort()
        score1 = war(naomi, ken)
        score2 = dwar(naomi,ken)
        #print("Case #"+str(i+1) + ": " + str(score2) + " " + str(score1) )
        fout.write("Case #"+str(i+1) + ": " + str(score2) + " " + str(score1) + "\n")
    fin.close()
    fout.close()
