import numpy

def output(number,count):
    print('Case #' + str(count) + ': ' + str(number))

def judge(number):
    digit = len(str(number))
    if digit == 1:
        result = number
        return result
    elif digit == 4:
        result = 999
        return result
    elif digit == 2:
        if (number % 10) >= int(number / 10):
            result = number
            return result
        else:
            result = number - (10 + number % 10) + 9
            return result
    elif digit == 3:
        hunderd = int(number / 100)
        ten = int((number - hunderd*100) / 10)
        one = number % 10
        '''
        if hunderd <= ten and ten <= one:
            result = number
            return result
        if hunderd > ten:
            result = (hunderd - 1) * 100 + 99
            return result
        elif ten > one:
            result = hunderd * 100 + (ten - 1) * 10 + 9
            return result
        '''
        if hunderd <= ten <= one:
            result = number
            return result
        elif hunderd > ten > one:
            result = (hunderd - 1) * 100 + 99
            return result
        elif hunderd > one > ten:
            result = (hunderd - 1) * 100 + 99
            return result
        elif ten > hunderd > one:
            result = hunderd * 100 + (ten - 1) * 10 + 9
            return result
        elif ten > one > hunderd:
            result = hunderd * 100 + (ten - 1) * 10 + 9
            return result
        elif one > hunderd > ten:
            result = (hunderd - 1) * 100 + 99
            return result

        elif ten > one == hunderd:
            result = hunderd * 100 + (ten - 1) * 10 + 9
            return result
        elif hunderd > ten == one:
            result = (hunderd - 1) * 100 + 99
            return result
        elif hunderd == ten > one:
            result = (hunderd - 1) * 100 + 99
            return result
        elif one == hunderd > ten:
            result = (hunderd - 1) * 100 + 99
            return result

c = input()
vector = []
count = 0;
for case in range(0,c):
    count = count + 1
    number = input()
    result = judge(number)
    output(result,count)