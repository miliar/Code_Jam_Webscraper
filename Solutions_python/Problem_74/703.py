
def calc(seq):
    index = 0
    time = 0
    pos = {'O': 1, 'B': 1}

    while 1:
        letter = seq[index][0]
        other_letter = [k for k in pos.keys() if k != letter][0]
        number = seq[index][1]
        
        pressed = False

        if number == pos[letter]:
            pressed = True
        else:
            if pos[letter] < number:
                pos[letter] += 1
            else:
                pos[letter] -= 1
        
        next = filter(lambda x: x[0] == other_letter, seq[index+1:])
        if next:
            next_pos = next[0][1]
            if pos[other_letter] == next_pos:
                pass
            elif pos[other_letter] < next_pos:
                pos[other_letter] += 1
            else:
                pos[other_letter] -= 1
        
        time += 1
        
        if pressed:
            if index == len(seq) - 1:
                break
            else:
                index += 1

    return time


fin = open('A-large.in')
fout = open('bots.out', 'w')


cases = int(fin.readline())

for case_index in range(cases):
    bits = fin.readline().strip().split()
    num = int(bits[0])
    bits = bits[1:]
    seq = []
    for i in range(num):
        seq.append((bits[i * 2], int(bits[i * 2 + 1])))
    time = calc(seq)
    fout.write('Case #%d: %d\n' % (case_index + 1, time))


fin.close()
fout.close()

