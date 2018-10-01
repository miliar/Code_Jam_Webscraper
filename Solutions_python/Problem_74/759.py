'''
Created on May 6, 2011

@author: Administrator
'''

def time(buttons):
    oButtons = [b for b in buttons if b[0] == 'O']

    bButtons = [b for b in buttons if b[0] == 'B']

    orangePOS = 1
    bluePOS = 1

    seconds = 0

    while buttons:
        seconds += 1

        bMoved, oMoved = False, False

        if bButtons and bluePOS < bButtons[0][1]:
            bluePOS += 1
            bMoved = True

        if oButtons and orangePOS < oButtons[0][1]:
            orangePOS += 1
            oMoved = True

        if bButtons and bluePOS > bButtons[0][1]:
            bluePOS -= 1
            bMoved = True

        if oButtons and orangePOS > oButtons[0][1]:
            orangePOS -= 1
            oMoved = True

        if oMoved and bMoved:
            continue

        if oButtons and oButtons[0] == buttons[0] and not oMoved:
            oButtons.pop(0)
            buttons.pop(0)
            continue

        if bButtons and bButtons[0] == buttons[0] and not bMoved:
            bButtons.pop(0)
            buttons.pop(0)

    return seconds



with open(r'data\A-large.in') as fhi, open(r'data\A-large.out', 'w') as fho:
    cases = int(fhi.readline())

    for case in range(cases):
        data = fhi.readline().rstrip().split(' ')

        pressCount = int(data.pop(0))

        buttons = [(data[i], int(data[i + 1])) for i in range(0, pressCount * 2, 2)]

        fho.write('Case #%d: %d\n' % (case + 1, time(buttons)))

