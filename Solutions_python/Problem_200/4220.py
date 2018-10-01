import random

def load_input(filename):
    file = open(filename, "r")

    file.readline()

    output = []
    while True:
        line = file.readline()
        if line == "":
            break
        else:
            output.append(int(line[:-1]))

    file.close()
    return output

def write(filename, input):
    file = open(filename, "w")

    for i in range(len(input)):
        file.write("Case #" + str(i + 1) + ": " + str(input[i]) + "\n")

    file.close()

def is_tidy(n):
    last = 0
    for char in str(n):
        if int(char) >= last:
            last = int(char)
        else:
            return False
    return True

def is_tidy2(n):
    if len(str(n)) == 1:
        return True
    last_left = 0
    last_right = 9
    for i in range(int(len(str(n))/2)):
        left = int(str(n)[i])
        right = int(str(n)[len(str(n))- i - 1])
        if  left > right or left < last_left or right > last_right:
            return False
        last_left = left
        last_right = right
    if len(str(n)) % 2 != 0:
        if int(str(n)[int(len(str(n)) / 2) - 1]) > int(str(n)[int(len(str(n)) / 2)]) or int(str(n)[int(len(str(n)) / 2)]) > int(str(n)[int(len(str(n)) / 2) + 1]):
            return False
    return True

def make_smaller(n):
    for i in range(len(str(n))):
        if not is_tidy(int(str(n)[:i+1])):
            return n - int(str(n)[i:]) - 1
    

def biggest_tidy(n):
    i = n
    while True:
        if is_tidy2(i):
            return i
        #print(i)
        i = make_smaller(i)

def tidy_numbers(list):
    output = []
    for n in list:
        output.append(biggest_tidy(n))
    return output

def test():
    n = random.randint(10 ** 17, 10 ** 18)
    print(n)
    print(biggest_tidy(n))

write("large2.out", tidy_numbers(load_input("B-large.in")))
