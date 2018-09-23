
# Load in file and split it up
file = open('example.in', 'r').read()
lines = file.splitlines()

inputs = int(lines[0])

pancakes = []; spatSizes = []

for line in lines[1:]:
    pancake, spatSize = line.split(' ')
    pancakes.append(pancake)
    spatSizes.append(int(spatSize))

# Change '+'s and '-'s to 1s and 0s
for lineIndex in range(len(pancakes)):
    pancakes[lineIndex] = list(pancakes[lineIndex])
    for stateIndex in range(len(pancakes[lineIndex])):
        if pancakes[lineIndex][stateIndex] == '+': pancakes[lineIndex][stateIndex] = 1
        else: pancakes[lineIndex][stateIndex] = 0
    pancakes[lineIndex] = pancakes[lineIndex]

# Do the math stuff
moves = []
for index in range(len(pancakes)):

    size = spatSizes[index]
    order = pancakes[index]

    move = 0
    for oIndex in range(len(order)):
        state = order[oIndex]

        if not state:
            move += 1

            # Is the flipper small enough?
            posLeft = len(order) - oIndex
            if posLeft < size: move = 'IMPOSSIBLE'; break

            # Change state of pancakes after
            for indexAdd in range(size):
                newIndex = oIndex + indexAdd

                if newIndex < len(order):
                    order[newIndex] = abs(order[newIndex] - 1)
                
    moves.append(move)


# for index in range(inputs):
#     print(spatSizes[index], pancakes[index], moves[index])

output = []
for index in range(len(moves)):
    value = 'Case #' + str(index + 1) + ': ' + str(moves[index])
    output.append(value)

out = '\n'.join(output)

writeFile = open('example.out', 'w')
writeFile.write(out)
writeFile.close