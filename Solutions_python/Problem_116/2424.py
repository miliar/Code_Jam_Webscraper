def game_check(element1, element2, element3, element4):
    if element1=='.' and element1==element2 and element2==element3 and element3==element4:
        return False
    elif element1==element2 and element2==element3 and element3==element4:
        return True
    elif element1=='T':
        if element2==element3 and element3==element4 and element2!='.':
            return True
    elif element2=='T':
        if element1==element3 and element3==element4 and element1!='.':
            return True
    elif element3=='T':
        if element1==element2 and element2==element4 and element1!='.':
            return True
    elif element4=='T':
        if element1==element2 and element2==element3 and element1!='.':
            return True
    else:
        return False


def list_check(li):
    #import pdb
    #pdb.set_trace()
    #for col in li:
     #   print col
    for a in xrange(4):
        checker = game_check(li[a][0], li[a][1], li[a][2], li[a][3])
        if checker:
            if li[a][0]=='T':
                return li[a][1]
            else:
                return li[a][0]
        checker = game_check(li[0][a], li[1][a], li[2][a], li[3][a])
        if checker:
            if li[0][a]=='T':
                return li[1][a]
            else:
                return li[0][a]
    checker = game_check(li[0][0], li[1][1], li[2][2], li[3][3])
    if checker:
        if li[0][0]=='T':
            return li[1][1]
        else:
            return li[0][0]
    checker = game_check(li[0][-1], li[1][-2], li[2][-3], li[3][-4])
    if checker:
        if li[0][-1]=='T':
            return li[1][-2]
        else:
            return li[0][-1]
    else:
        if ('.' in li[0]) or ('.' in li[1]) or ('.' in li[2]) or ('.' in li[3]):
            return "NotOver"
        else:
            return "Draw"


filename = "test-large.in"
fh = open(filename, "r")
T = int(fh.readline())
counter = 0
stats  = [[]]*T
while counter < T:
    temp = []
    for i in xrange(4):
        temp.append(list(fh.readline().strip('\n')))
    fh.readline()
    stats[counter] = temp
    counter += 1

out = open("out.out", "w")
for counter in xrange(T):
    winner = list_check(stats[counter])
    if winner == 'X':
        out.write("Case #%d: X won\n" % (counter+1))
    elif winner == 'O':
        out.write("Case #%d: O won\n" % (counter+1))
    elif winner == "Draw":
        out.write("Case #%d: Draw\n" % (counter+1))
    elif winner == "NotOver":
        out.write("Case #%d: Game has not completed\n" % (counter+1))
