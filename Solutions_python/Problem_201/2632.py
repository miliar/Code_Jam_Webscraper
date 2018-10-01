from sys import argv
import operator

"""
A certain bathroom has N + 2 stalls in a single row; the stalls on the left and right ends are permanently occupied by the bathroom guards. The other N stalls are for users.

Whenever someone enters the bathroom, they try to choose a stall that is as far from other people as possible. To avoid confusion, they follow deterministic rules: For each empty stall S, they compute two values LS and RS, each of which is the number of empty stalls between S and the closest occupied stall to the left or right, respectively. Then they consider the set of stalls with the farthest closest neighbor, that is, those S for which min(LS, RS) is maximal. If there is only one such stall, they choose it; otherwise, they choose the one among those where max(LS, RS) is maximal. If there are still multiple tied stalls, they choose the leftmost stall among those.

K people are about to enter the bathroom; each one will choose their stall before the next arrives. Nobody will ever leave.

When the last person chooses their stall S, what will the values of max(LS, RS) and min(LS, RS) be?
"""

class Bathrooms:
    def __init__(self, filename, output_filename):
        self.input_filename = filename
        self.output_filename = output_filename
        self.test_cases = self.read_file()
        self.write_handler = open(self.output_filename, 'w')

    def read_file(self):
        print "Opening %r to read assembly." % self.input_filename
        file_handler = open(self.input_filename, 'r')
        return file_handler.read().splitlines()

    def calculate_stall_choice(self, num_stalls, num_people):
        # print "Num stalls: %i" % num_stalls
        # print "Num people: %i" % num_people
        if num_stalls == num_people:
            return 0, 0
        elif (num_people > ((num_stalls // 2) + 50)):
            return 0, 0

        stalls = ['o'] + [None]*num_stalls + ['o']
        occupied_stall_indices = [0, len(stalls)-1]
        i = 0

        while i < num_people:
            stalls = self.calculate_stall_distances(stalls, occupied_stall_indices)
            index_to_occupy, max_min, max_max = self.choose_stall(stalls)
            occupied_stall_indices.append(index_to_occupy)
            stall_chosen = stalls[index_to_occupy]
            stalls[index_to_occupy] = 'o'
            i += 1
        # print "Final stall configuration: "
        # print stalls
        return max(stall_chosen), min(stall_chosen)

    def calculate_stall_distances(self, stalls, occupied_stall_indices):
        for index, stall in enumerate(stalls):
            if stall == 'o':
                last_seen_occupied = index
                left_counter = 0
                right_counter = self.initialize_right_counter(index, occupied_stall_indices) - 1
            else: 
                stalls[index] = [left_counter, right_counter]
                right_counter -= 1
                left_counter += 1
        return stalls


    def max_left_right(self, stalls):
        max_distances = {}
        for idx, stall in enumerate(stalls):
            if stall != 'o':
                if max(stall) in max_distances:
                    max_distances[max(stall)].append(idx)
                else:
                    max_distances[max(stall)] = [idx]
        max_maximum_distance = max(max_distances.keys())
        sequential_indices = []
        distances = max_distances[max_maximum_distance]
        for idx, val in enumerate(distances[1:], start=1):
            if val - distances[idx-1] == 1:
              sequentail_indices = [idx, idx-1]
        if len(sequential_indices) == 0:
            index_of_max_max_distance = min(max_distances[max_maximum_distance])
        else:
            index_of_max_max_distance = min(sequential_indices)
        # print distances
        # print sequential_indices
        return max_maximum_distance, index_of_max_max_distance

    def min_left_right(self, stalls):
        min_distances = {}
        for idx, stall in enumerate(stalls):
            if stall != 'o':
                if min(stall) in min_distances:
                    min_distances[min(stall)].append(idx)
                else:
                    min_distances[min(stall)] = [idx]
        # print min_distances
        max_min_distance = max(min_distances.keys())
        sequential_indices = []
        distances = min_distances[max_min_distance]
        for idx, val in enumerate(distances[1:], start=1):
            if val - distances[idx-1] == 1:
              sequential_indices = [val, distances[idx-1]]
        # print distances
        # print "sequential indices: ", sequential_indices
        if len(sequential_indices) == 0:
            index_of_max_min_distance = min(min_distances[max_min_distance])
        else:
            # print "using sequential indices"
            index_of_max_min_distance = min(sequential_indices)
            # print "index of max_min_distance", index_of_max_min_distance

        return max_min_distance, index_of_max_min_distance

    def choose_stall(self, stalls):
        # print stalls
        max_minimum_distance, idx_of_max_min_distance = self.min_left_right(stalls)
        max_maximum_distance, idx_of_max_max_distance = self.max_left_right(stalls)

        if max_minimum_distance == 0:
            index_to_occupy = idx_of_max_max_distance
        else:
            index_to_occupy = idx_of_max_min_distance

        # print "index %i; with max_max of %i and max_min of %i" % (index_to_occupy, max_maximum_distance, max_minimum_distance)
        return index_to_occupy, max_minimum_distance, max_maximum_distance

    def initialize_right_counter(self, current_index, occupied_stalls):
        stalls_to_the_right = []
        for stall_idx in occupied_stalls:
            if current_index < stall_idx:
                stalls_to_the_right.append(stall_idx)
        if len(stalls_to_the_right) > 0:
            right_counter = min(stalls_to_the_right) - current_index - 1
        else:
            right_counter = 0
        return right_counter

    def calculate_max_min_sides(self):
        for index, case in enumerate(self.test_cases[1:], start=1):
            num_stalls, num_people = case.split(' ')
            max_l_r, min_l_r = self.calculate_stall_choice(int(num_stalls), int(num_people))
            result_str = "Case #%i: %i %i" % (index, max_l_r, min_l_r)
            print result_str
            self.write_handler.write(result_str + "\n")


script, filename, out_file = argv
Bathrooms(filename, out_file).calculate_max_min_sides()

