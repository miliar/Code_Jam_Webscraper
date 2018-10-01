import sys

def solve(cards, rows):
    cards_a = cards[0][rows[0] - 1]
    cards_b = cards[1][rows[1] - 1]
    answer = set(cards_a).intersection(set(cards_b))
    if len(answer) == 0:
        return "Volunteer cheated!"
    elif len(answer) > 1:
        return "Bad magician!"
    else:
        return str(answer.pop())

def numeric_cards(lines):
    cards = []
    for line in lines:
        cards.append(tuple([int(i) for i in line.split(' ')]))
    return tuple(cards)
    
def main(argv):
    input = ''
    try:
        input = open(argv[1]).read()
    except:
        print 'Invalid Usage'
        print 'Usage %s <input file>' % (argv[0], )
        return
    
    lines = input.splitlines()
    test_case = lines[0]
    lines = lines[1:]
    for i in xrange(len(lines)/10):
        case = ((numeric_cards(lines[1+i*10:1+i*10+4]), numeric_cards(lines[6+i*10:6+i*10+4])), (int(lines[i*10]), int(lines[5+i*10])))
        print "Case #%d: %s" % (i + 1, solve(*case))
        
if __name__ == '__main__':
    main(sys.argv)