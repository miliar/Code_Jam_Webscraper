problem = 'BotTrust'
t = 'l'
debug = False

middle = {'t': 'ex', 's': 'small', 'l': 'large'}[t]

input_file = open('{problem}-{middle}.in'.format(**globals()))
output_file = open('{problem}-{middle}.out'.format(**globals()), 'w')

import decimal

# Helper functions
def split_to_ints(s):
    return [i for i in map(int, s.split())]

def list_to_index_tuple(l, base=0):
    return [(i + base, l[i]) for i in range(len(l))]

class Solution:
    format = '{0}' # The format string for solutions
    
    def __init__(self, get):
        # Read in the entire solution
        self.buttons = get().split()
    
    def weight(self):
        # Return the value that determines the weight of the solution (for timing)
        return int(self.buttons[0])
    
    def solve(self):
        # Return the solution dictionary for this case
        steps = ((self.buttons[2*i+1], int(self.buttons[2*i+2])) for i in range(int(self.buttons[0])))
        last_bot = ''
        o_button = 1
        b_button = 1
        o_time = 0
        b_time = 0
        time = 0
        for step in steps:
            cur_bot = step[0]
            cur_button = step[1]
            if cur_bot == 'O':
                time = max(o_time + abs(cur_button - o_button), time) + 1
                o_time = time
                o_button = cur_button
            else:
                time = max(b_time + abs(cur_button - b_button), time) + 1
                b_time = time
                b_button = cur_button
        return time
    
if debug: from time import clock
    
if __name__ == '__main__':
    get = input_file.readline
    n = int(get())
    durations = []
    for i in range(n):
        s = Solution(get)
        if debug:
            print ('Case {} started'.format(i))
            start = clock()
        o = s.format.format(s.solve())
        if debug:
            duration = clock() - start
            durations += [(duration, s.weight())]
            print ('Case {} solved in {}'.format(i, durations[-1][0]))
            print ('Weight {}, so: {}'.format(durations[-1][1], durations[-1][0] / durations[-1][1]))
        output_file.write('Case #{}: {}\n'.format(i+1, o))
    if debug:
        mean = sum(x[0] for x in durations) / len(durations)
        maxdiff = 0
        for x in durations:
            maxdiff = max(maxdiff, abs(mean-x[0]))
        if maxdiff/mean < .25: print('O(1)')
        else: print('> O(1)')
        mean = sum(x[0]/x[1] for x in durations) / len(durations)
        maxdiff = 0
        for x in durations:
            maxdiff = max(maxdiff, abs(mean-(x[0]/x[1])))
        if maxdiff/mean < .25: print('O(N)')
        else: print('> O(N)')
        