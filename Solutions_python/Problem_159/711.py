def first_method(mushroom_count, length):
    eaten = 0
    for i in range(length-1):
        diff = mushroom_count[i] - mushroom_count[i+1]
        if diff > 0:
            eaten += diff
    return eaten

def second_method(mushroom_count, length):
    eaten = 0
    rate = 0
    for i in range(length-1):
        diff = mushroom_count[i] - mushroom_count[i+1]
        if diff > rate:
            rate = diff
    for i in range(length-1):
        diff = mushroom_count[i] - mushroom_count[i+1]
        if mushroom_count[i] < rate:
            eaten += mushroom_count[i]
        else:
            eaten += rate
    return eaten

input_file = open('A-large.in', 'r')
source = input_file.read()
source = source.splitlines()
input_file.close()
output = open('A-output-large.txt', 'w')
for i in range(int(source[0])):
    output.write('Case #%d: '%(i+1))
    mushroom_count = source[i*2+2].split()
    length = int(source[i*2+1])
    for i in range(length):
        mushroom_count[i] = int(mushroom_count[i])
    output.write(str(first_method(mushroom_count, length)) + ' ' +
                 str(second_method(mushroom_count, length)) + '\n')
output.close()
