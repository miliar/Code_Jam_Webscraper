def solve(list1, list2):
    def count_winnings(_list1,_list2):
        winnings = 0
        for i in range(len(_list1)):
            if (_list1[i]>_list2[i]):
                winnings+=1
        return winnings
    def fair_game(_list1, _list2):
        winnings = 0
        l2 = _list2[:]
        l2.reverse()
        for i in range(len(_list1)):
            for j in range(len(l2)):
                if l2[j]>_list1[i]:
                    l2.remove(l2[j])
                    break
            #print len(l2), len(_list1)-i
            if len(l2)>=len(_list1)-i:
                l2.remove(l2[0]) #remove smallest
                winnings+=1
        return winnings
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    max_war = [fair_game(list1,list2)]
    max_dec_war = [count_winnings(list1, list2)]
    for i in range(len(list2)-1):
        item = list1[-1]
        list1.remove(item)
        list1.insert(i,item)
##        print '!', list1
##        print list2
##        print count_winnings(list1, list2)
        max_dec_war.append(count_winnings(list1,list2))
        max_war.append(fair_game(list1,list2))
    return (max(max_dec_war), max(max_war))

with open('D-small-attempt0.in', 'r') as f:
    inp = f.readlines()
    f.close()
##inp = raw_input().split('\n')
line_counter = 0
T = int(inp[line_counter])
line_counter+=1
data = ''
for i in range(T):
    n = int(inp[line_counter])
    line_counter+=1
    naomi = []
    for _inp in inp[line_counter].split(' '):
        naomi.append(float(_inp))
    line_counter+=1
    ken = []
    for _inp in inp[line_counter].split(' '):
        ken.append(float(_inp))
    line_counter+=1
    out = solve(naomi,ken)
    data += 'Case #%d: %d %d\n' %(i+1, out[0], out[1])
with open('output.txt', 'w') as f:
    f.write(data)
    f.close()
print data
