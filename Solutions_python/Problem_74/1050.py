# robot name, cur_pos, next_move
robot_O = ['O', 1, 1]
robot_B = ['B', 1, 1]

def goTo(x, robot):
    if robot[1] == x:
        if robot[0] == 'O':
            free_move(robot_B)
        else:
            free_move(robot_O)
        return 0
    else:
        move_cost = abs(x - robot[1])
        for i in range(1, move_cost + 1):
            if robot[0] == 'O':
                free_move(robot_B)
            else:
                free_move(robot_O)
        robot[1] = robot[2] = x
        return move_cost

def push_x(x, robot):
    if robot[0] == 'O':
        free_move(robot_B)
    else:
        free_move(robot_O)
    if robot[1] == x:
        return 1
    else:
        return goTo(x, robot) + 1

def free_move(r):
    if r[0] == 'B':        
        if robot_B[2] != robot_B[1]:
            if robot_B[2] > robot_B[1]:
                robot_B[1] = robot_B[1] + 1 # peut être - 1 selon sens
            else:
                robot_B[1] = robot_B[1] - 1
    else:
        if robot_O[2] != robot_O[1]:
            if robot_O[2] > robot_O[1]:
                robot_O[1] = robot_O[1] + 1
            else:
                robot_O[1] = robot_O[1] - 1
        
def robot_push(x, r):
    return push_x(x, r)

def cas(i, s):
    print('Case #{}: {}'.format(i, s))
   
# import doctest    
# doctest.testmod()
T = int(input())
for tc in range(1, T + 1):
    robot_O = ['O', 1, 1]
    robot_B = ['B', 1, 1]
    cheptel = {}
    li = input().split()
    l = [x for x in li[1:]]
# 4 O 2 B 1 B 2 O 4 => 6
#    l = '4 O 2 B 1 B 2 O 4'.split()[1:]
#    l = '3 O 5 O 8 B 100'.split()[1:]
# l = '2 B 2 B 1'.split()[1:]
    robots = []
    buttons = []
    for i in range(0, len(l), 2):
        robots.append(l[i])
    for j in range(1, len(l), 2):
        buttons.append(l[j])
    ordres = []
    for k in range(0, len(robots)):
        ordres = ordres + [(robots[k], int(buttons[k]))]

    seconds = 0    
    cheptel = {'O': robot_O, 'B': robot_B}
    for s in range(0, len(ordres)):
        if ordres[s][0] == 'O':        
            for nb in range(s + 1, len(ordres)):
                if ordres[nb][0] == 'B':
                    robot_B[2] = ordres[nb][1]
                    break
        else:
            for no in range(s + 1, len(ordres)):
                if ordres[no][0] == 'O':
                    robot_O[2] = ordres[no][1]
                    break
        (nom, btn) = ordres[s]
        seconds = seconds + robot_push(btn, cheptel[nom])
    cas(tc, seconds)

