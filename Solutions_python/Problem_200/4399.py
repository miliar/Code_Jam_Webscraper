import sys

def tidy(number):
    previous = -1
    for num in number:
        if previous == -1:
            previous = num
        else:
            if num < previous:
                return False
            previous = num
    return True

with open(sys.argv[1]) as file:
    next(file)
    counter = 0
    for line in file:
        counter += 1
        number = int(line)
        reversed_string = line[::-1]
        if number < 10 or tidy(str(number)):
            print "Case #" + str(counter).strip() + ": " + str(number).strip()
            continue
        else:
            minus = ""
            previous = -1
            for c in reversed_string:
                if previous == -1:
                    previous = c
                else:
                    if c >= previous:
                        minus += previous
                    previous = c
            minus = minus[::-1]
        number = number - int(minus)
        while(number > 0):
            if(tidy(str(number))):
                print "Case #" + str(counter).strip() + ": " + str(number).strip()
                break
            number -= 1
