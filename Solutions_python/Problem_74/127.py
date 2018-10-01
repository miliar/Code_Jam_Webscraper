#!/usr/bin/python


def solve(actions):
    t_prev = [ 0, 0 ] # endtime of last action for each robot
    p_prev = [ 1, 1 ] # position of last action for each robot
    global_t_prev = 0 # endtime of last action
    for bot, button in actions:
        already_there = global_t_prev + 1
        need_to_move = t_prev[bot] + abs(p_prev[bot] - button) + 1
        best_time = max(already_there, need_to_move)

        # print "bot=%d button=%d already_there=%d need_to_move=%d best_time=%d" %\
        #         (bot, button, already_there, need_to_move, best_time)

        t_prev[bot] = best_time
        p_prev[bot] = button
        global_t_prev = best_time
    return global_t_prev

    
if __name__ == "__main__":
    import sys
    tests = int(sys.stdin.readline())
    for t in range(tests):
        line = sys.stdin.readline().split()
        n = int(line[0])
        assert len(line) == 2 * n + 1
        actions = []
        for i in range(n):
            bot = line[1 + 2 * i]
            bot = {'O': 0, 'B': 1}[bot]
            button = int(line[1 + 2 * i + 1])
            actions.append((bot, button))
        result = solve(actions)
        print "Case #%d: %d" % (t + 1, result)

            
