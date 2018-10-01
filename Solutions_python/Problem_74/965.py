def main():
    test_num = int(raw_input())
    for i in range(test_num):
        string = raw_input()
        input_list = string.split()
        pos_num = int(input_list[0])
        input_list.remove(input_list[0])
        print "Case #%d: %d" % (i+1, solve(pos_num, input_list))

    
def solve(pos_num, input_list):
    pos_list = []
    pos_list.append([])
    pos_list.append([])
    turn_list = []
    
    for j in range(pos_num):
        if input_list[2*j] == 'O':
            turn_list.append('O')
            pos_list[0].append(int(input_list[2*j+1]))
        elif input_list[2*j] == 'B':
            turn_list.append('B')
            pos_list[1].append(int(input_list[2*j+1]))

    pos = [1, 1]
    if len(pos_list[0])==0:
        push = [0, pos_list[1][0]]
    elif len(pos_list[1])==0:
        push = [pos_list[0][0], 0]
    else:
        push = [pos_list[0][0], pos_list[1][0]]
    idx = [0, 0]

    cur_turn = turn_list[0]
    sec = 0

    for bot in turn_list:
        if bot == 'O':
            x = 0
            y = 1
        else:
            x = 1
            y = 0

        # x: current bot that has to push the button
        while push[x] != pos[x]:
            if push[x] > pos[x]:
                pos[x]+=1
            elif push[x] < pos[x]:
                pos[x]-=1

            if push[y] > pos[y]:
                pos[y]+=1
            elif push[y] < pos[y]:
                pos[y]-=1

            sec += 1

        #push
        idx[x]+=1
        if idx[x]<len(pos_list[x]):
            push[x] = pos_list[x][idx[x]]
        if push[y] > pos[y]:
            pos[y]+=1
        elif push[y] < pos[y]:
            pos[y]-=1
        sec += 1

    return sec

    

if __name__=="__main__": main()
