import sys

def flip(pancakes, start, capacity):
    new_pancakes = pancakes[:]
    for index in range(0, capacity):
        new_pancakes[start + index] = "-" if new_pancakes[start + index] == "+" else "+"
    return new_pancakes

def find_flippable(pancake, capacity):
    #print pancake
    sad_index =  [i for i, val in enumerate(pancake[:-capacity]) if val == "-"]
    if "-" in pancake[-capacity:]:
        sad_index.append(len(pancake) - capacity)
    return sad_index
def find_smallest_step(pancakes, capacity):
    queue = []
    visited = []
    queue.append((pancakes,0))
    test = 0
    visited.append(pancakes)
    while(len(queue) != 0):
        test += 1
        state = queue.pop(0)
        current_pancake = state[0]
        step = state[1]
        #print queue
        if "-" not in current_pancake : return step
        #print find_flippable(current_pancake, capacity), current_pancake, step
        for pancake_index in find_flippable(current_pancake, capacity):
            flipped = flip(current_pancake, pancake_index, capacity)
            if flipped not in visited:
                visited.append(flipped)
                #print flipped, step
                queue.append((flipped, step + 1))
    #print test
    return "IMPOSSIBLE"

input_count = int(raw_input())
index = 1
while (input_count > 0):
    cur_line = raw_input().split()
    capacity = cur_line[1]
    pancakes = cur_line[0]
    sys.stdout.write("Case #{}: {}\n".format(str(index), str(find_smallest_step(list(pancakes), int(capacity)))))
    input_count -= 1
    index += 1
