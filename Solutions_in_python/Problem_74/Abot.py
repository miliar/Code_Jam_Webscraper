#!/usr/bin/python3

from sys import argv

def sign(n):
    if n == 0: return 0
    elif n > 0: return 1
    else: return -1

def bluebutt(button):
    for i in range(button, len(bot)):
        if bot[i] == 'B':
            return num[i]
    return 0

def oranbutt(button):
    for i in range(button, len(bot)):
        if bot[i] == 'O':
            return num[i]
    return 0

bot, num = [], []

infile = open(argv[1])
cases = int(infile.readline())
for i in range(0, cases):
    line = infile.readline()
    vals = line.split()[1:]
    bot, num = [],[]
    for j in range(0, len(vals), 2):
        button = j // 2
        bot.append(vals[j])
        num.append(int(vals[j+1]))
    o, b, button, time = 1, 1, 0, 0
    while True:
        time += 1
        if bot[button] == 'O':
            if o == num[button]:
                button += 1
            else:
                o += sign(num[button] - o)
            bbutt = bluebutt(button)
            b += sign(bbutt - b)
        else:
            if b == num[button]:
                button += 1
            else:
                b += sign(num[button] - b)
            obutt = oranbutt(button)
            o += sign(obutt - o)
        if button == len(bot):
            break
    print('Case #{}: {}'.format(i+1, time))
