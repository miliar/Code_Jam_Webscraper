#!/usr/bin/python

import string
import sys

def solve(input, output):
    for i in range(int(input.readline())):
        case = input.readline().split(' ')

        # process combos
        combos = dict()
        combo_count = int(case.pop(0))
        for j in range(combo_count):
            combo_chars = list(case.pop(0))
            if combo_chars[0] not in combos:
                combos[combo_chars[0]] = dict()
            if combo_chars[1] not in combos:
                combos[combo_chars[1]] = dict()
            combos[combo_chars[0]][combo_chars[1]] = combo_chars[2]
            combos[combo_chars[1]][combo_chars[0]] = combo_chars[2]

        # process oppos
        oppos = dict()
        oppo_count = int(case.pop(0))
        for j in range(oppo_count):
            oppo_chars = list(case.pop(0))
            if oppo_chars[0] not in oppos:
                oppos[oppo_chars[0]] = dict()
            if oppo_chars[1] not in oppos:
                oppos[oppo_chars[1]] = dict()
            oppos[oppo_chars[0]][oppo_chars[1]] = 1
            oppos[oppo_chars[1]][oppo_chars[0]] = 1

        print oppos

        # process the real deal
        case.pop(0)
        invoke_chars = list(case.pop(0))
        result_chars = list()
        for invoke_char in invoke_chars:
            print 'invoke_char = %s' % (invoke_char)
            if len(result_chars) == 0:
                if invoke_char != '\n':
                    result_chars.append(invoke_char)
                    print 'append'
            else:
                if invoke_char in combos and \
                    result_chars[-1] in combos[invoke_char]:
                    print 'combo %s %s = %s' % (invoke_char, result_chars[-1],\
                        combos[invoke_char][result_chars[-1]])
                    result_chars[-1] = combos[invoke_char][result_chars[-1]]
                elif invoke_char in oppos:
                    for cur_char in result_chars:
                        if cur_char in oppos[invoke_char]:
                            print 'oppo %s %s' % (invoke_char, cur_char)
                            result_chars = list()
                            break
                    if len(result_chars) > 0:
                        result_chars.append(invoke_char)
                        print 'append'
                elif invoke_char != '\n':
                    result_chars.append(invoke_char)
                    print 'append'
            print 'cur result: %s' % (result_chars)

        print 'Case #%d: [%s]' % (i+1, ', '.join(result_chars))
        output.write('Case #%d: [%s]\n' % (i+1, ', '.join(result_chars)))

def main():
    in_file = sys.argv[1]
    input = open(in_file)
    output = open(in_file + '.result', 'w')

    solve(input, output)

    input.close()
    output.close()

if __name__ == '__main__':
    main()
