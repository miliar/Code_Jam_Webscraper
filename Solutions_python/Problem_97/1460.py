import fileinput

def recycled_numbers(a, b):
    result = 0
    for low in range(a, b):
        for high in range(low+1, b+1):
            if is_recycled(low, high):
                result += 1
    return result

def is_recycled(low, high):
    for pos in range(len(str(high))):
        if str(low) == (str(high)[pos:] + str(high)[:pos]):
            return True
    return False

def main():
    for line in fileinput.input():
        if fileinput.isfirstline():
            continue
        line = line.split()
        result = recycled_numbers(int(line[0]), int(line[1]))
        print("Case #{}: {}".format(fileinput.lineno()-1, result))

if __name__ == '__main__':
    main()
