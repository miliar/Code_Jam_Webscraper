
def get_cards():
    cards = []
    for i in range(4):
        row = raw_input().split(' ')
        row = [int(i) for i in row]
        cards.append(row)
    return cards

def solve_test_case(test_case_number):
    first_row = int(raw_input()) - 1
    first_cards = get_cards()
    second_row = int(raw_input()) - 1
    second_cards = get_cards()
    
    intersection = list(set(first_cards[first_row]).intersection(set(second_cards[second_row])))
    l = len(intersection)
    if l == 1:
        print 'Case #%d: %d' % (test_case_number, intersection[0])
    elif l > 0:
        print 'Case #%d: Bad magician!' % (test_case_number, )
    else:
        print 'Case #%d: Volunteer cheated!' % (test_case_number, )
        
number_of_cases = int(raw_input())
for i in range(1, number_of_cases + 1):
    solve_test_case(i)
