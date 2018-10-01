import ast

def tidy(numbers):
    index = 1
    while index < len(numbers):
        if numbers[index] >= numbers[index-1]:
            index += 1
        else:
            index -=1
            numbers[index] -=1

            while index > 0 and numbers[index] < numbers[index -1]:
                index -=1
                numbers[index] -=1

            if index == 0 and numbers[index]==0:
                numbers = numbers[1:]
                index -= 1

            index += 1
            return "".join(str(n) for n in (numbers[:index]+[9 for number in numbers[index:]]))

    return "".join(str(n) for n in numbers)


with open("B-large.in", 'r') as input:
    lines = input.readlines()
    cases = lines[1:]

with open("output.txt", 'w') as output:
    index = 1
    for case in cases:

        output.write("Case #{i}: {result}\n".format(i=index, result=tidy([int(c) for c in str(ast.literal_eval(case))])))
        index +=1
