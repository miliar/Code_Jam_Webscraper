import fileinput
from collections import deque

class Dupestring:
    data = []

    def num_actions(self, x):
        # Guarantee similarity
        if (not self.similar(x)):
            return None

        total_actions = 0
        for i in range(len(self.data)):
            total_actions += abs(self.data[i][1] - x.data[i][1])

        return total_actions

    def equals(self, x):
        # Check for similarity first
        if (not self.similar(x)):
            return False

        # Check for correct numbers of occurences
        for i in len(self.data):
            if (self.data[i][1] != x.data[i][1]):
                return False

        # Return true when it passes the tests
        return True

    def similar(self, x):
        # Check for similar lengths
        if (len(self.data) != len(x.data)):
            return False

        # Check for correct characters
        for i in range(len(self.data)):
            if (self.data[i][0] != x.data[i][0]):
                return False

        # Return true when it passes the tests
        return True

    def empty(self):
        if (len(self.data) == 0):
            return True
        else:
            return False

    def destroy(self):
        self.data = []

    def string_set(self):
        s = ''
        for i in self.data:
            s += i[0]

        return s

    def __init__(self, s):
        if (not self.empty()):
            self.destroy()

        # For each character in the string s
        for c in s:
            # If not a duplicate character, append character information
            if (self.empty() or self.data[-1][0] != c):
                self.data.append([c, 1])
            # If a duplicate character, append number of occurences
            else:
                self.data[-1][1] += 1

    def __repr__(self):
        s = ''
        for i in self.data:
            for j in range(i[1]):
                s += i[0]

        return s

def get_answer(input_num, dupestrings):
    # Build answer string
    answer = 'Case #'+str(i+1)+': '

    # Check for possbility
    for d1 in dupestrings:
        for d2 in dupestrings:
            if (not d1.similar(d2)):
                answer += 'Fegla Won'
                return answer

    lowest_total = None
    # Check totals
    for d in dupestrings:
        cur_total = get_total(d, dupestrings)
        if (cur_total < lowest_total) or (lowest_total == None):
            lowest_total = cur_total

    # Create a dummy minimum object
    minstring = Dupestring(dupestrings[0].string_set())

    # Check for min string case
    cur_total = get_total(minstring, dupestrings)
    if (cur_total < lowest_total) or (lowest_total == None):
        lowest_total = cur_total

    answer += str(lowest_total)

    return answer

def get_total(chosen, others):
    total = 0

    for o in others:
        total += chosen.num_actions(o)

    return total


num_inputs = 0
lines = deque()

for line in fileinput.input():
    lines.append(line)

num_inputs = int(lines.popleft())

# Get inputs
for i in range(num_inputs):
    dupestrings = []
    strings  = []
    del strings[:]
    del dupestrings[:]
    num_strings = int(lines.popleft())
    # Get raw strings
    for j in range(num_strings):
        strings.append(lines.popleft().strip())
    # Build objects
    for s in strings:
        dupestring = Dupestring(s)
        dupestrings.append(dupestring)

    # Find the answer
    print(get_answer(i+1, dupestrings))

