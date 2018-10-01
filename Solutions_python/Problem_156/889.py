from math import ceil, floor

filename = "pancakes.in"


f = open(filename, "r")
num_test_cases = int(f.readline().strip())

# start with an optimal time of max(plates)
# have "optimization rounds"
#   in each round, start from the middle of the first plate upwards
#   cut the entire pancake triangle horizontally: take note of the new max height and the number of relocations needed
#   (the number of pancake stacks above the cut height)
#   if the "new" optimal time: the new max stack height + number of relocations < optimal time, apply the change
#       then start a new optimization round
#   else continue upwards
# end optimization rounds when there is a round where not optimization is made


# simulates cutting pancakes at height (the new max stack is height high)
def count_cuts_at_height(plates, height):
    count = 0
    for plate in plates:
        if plate <= height:
            break
        count += 1
    return count


# actually cuts the stacks at height
# cut as low as it goes: if a height ends in the middle of everything, lower the height as much as you can, without cutting another
def cut_at_height(plates, height, cut_as_low_as_it_goes=False):
    # get a lower height if requested
    if cut_as_low_as_it_goes:
        initial_cuts = count_cuts_at_height(plates, height)
        while True:
            if height != 1 and count_cuts_at_height(plates, height - 1) == initial_cuts:
                height -= 1
            else:
                break

    while plates[0] > height:
        # split the biggest pancake
        biggest_plate = plates[0]
        del plates[0]

        # insert split plate values to their sorted posititons
        for value in (height, biggest_plate - height):
            # handle empty
            if not plates:
                plates.append(value)
                continue

            inserted = False
            for i in range(len(plates)):
                if plates[i] <= value:
                    plates.insert(i, value)
                    inserted = True
                    break
            if not inserted:
                plates.append(value)


# search the whole problem space
# pancakes are always sorted
# returns (num_rounds, pancake_stack) for the best solution found
def bruteforce_search(pancakes, startmax, specialrounds=0):
    current_time = pancakes[0] + specialrounds

    # end recursion when there is nothing to split
    if pancakes[0] == 1 or specialrounds > startmax:
        return current_time, pancakes

    # relocate pancakes from the biggest pile, but only to the half (we start repeating then)
    times = []
    pancake_stacks = []
    half = ceil(pancakes[0] / 2)
    for base_height in range(half, pancakes[0]):
        # split a new pancake list by the criterion
        new_pancakes = list(pancakes)
        biggest_plate = new_pancakes[0]
        del new_pancakes[0]

        # insert split plate values to their sorted posititons
        for value in (base_height, biggest_plate - base_height):
            # handle empty
            if not new_pancakes:
                new_pancakes.append(value)
                continue

            inserted = False
            for i in range(len(new_pancakes)):
                if new_pancakes[i] <= value:
                    new_pancakes.insert(i, value)
                    inserted = True
                    break
            if not inserted:
                new_pancakes.append(value)
        time, pancake_stack = bruteforce_search(new_pancakes, startmax, specialrounds + 1)
        times.append(time)
        pancake_stacks.append(pancake_stack)

    # find the minimum of all children, return both the time and the pancake stack
    min_time = times[0]
    min_index = 0
    for idx, time in enumerate(times):
        if time < min_time:
            min_time = time
            min_index = idx

    if min_time >= current_time:
        return current_time, pancakes

    return min_time, pancake_stacks[min_index]



def case(test_case):
    num_diners = int(f.readline().strip())
    plates = [int(a) for a in f.readline().strip().split(" ")]
    plates.sort(reverse=True)
    print(plates)
    t, pcks = bruteforce_search(list(plates), plates[0])


    optimal_time = plates[0]  # the initial time is the same as the number of pancakes on the biggest plate
    total_cuts = 0

    # optimization passes
    while True:
        optimization_made = False

        half = ceil(plates[0] / 2)

        # reduce the cut height every time (increase the base height)
        for base_height in range(half, plates[0]):
            cuts = count_cuts_at_height(plates, base_height)
            if base_height + total_cuts + cuts < optimal_time:
                cut_at_height(plates, base_height)
                optimal_time = base_height + total_cuts + cuts
                total_cuts += cuts
                optimization_made = True
                break

        if not optimization_made:
            break

    if optimal_time != t:
        print("ALEEEEEEEEEEEEEEEERT")
    print("Case #{}: {}".format(test_case, optimal_time))
    print("    {}".format(plates))
    print("  bruteforce: {}".format(t))
    print("    {}".format(pcks))
    print()


def bruteforce_case(test_case):
    num_diners = int(f.readline().strip())
    plates = [int(a) for a in f.readline().strip().split(" ")]
    plates.sort(reverse=True)
    t, pcks = bruteforce_search(list(plates), plates[0])
    print("Case #{}: {}".format(test_case, t))



# each test case
for test_case in range(1, num_test_cases + 1):
    # case(test_case)
    bruteforce_case(test_case)





# # each test case
# for test_case in range(1, num_test_cases + 1):
#     num_diners = int(f.readline().strip())
#     plates = [int(a) for a in f.readline().strip().split(" ")]
#     plates.sort(reverse=True)
#
#     max_time = plates[0]  # the initial time is the same as the number of pancakes on the biggest plate
#     special_rounds = 0
#
#     while True:
#         # split the biggest pancake
#         biggest_plate = plates[0]
#         del plates[0]
#
#         # insert split plate values to their sorted posititons
#         for value in (int(ceil(biggest_plate / 2)), int(floor(biggest_plate / 2))):
#             # handle empty
#             if not plates:
#                 plates.append(value)
#                 continue
#
#             for i in range(len(plates)):
#                 if plates[i] <= value:
#                     plates.insert(i, value)
#                     break
#
#         # check if the split was beneficial
#         # move pancakes while the new projected time is smaller than the current max time
#         # the new projected time is the biggest plate, plus the number of special rounds used, plus an additional round
#         if plates[0] + special_rounds + 1 > max_time:
#             break
#
#         # if the move was beneficial, use this special round
#         special_rounds += 1
#         max_time = plates[0] + special_rounds
#
#     # print the complete time taken
#     print("Case #{}: {}".format(test_case, max_time))
