'''
Created on Apr 13, 2014

@author: Kevin Bui (huy.buiquang72@gmail.com)
'''

def solve(case):
    result = 0
    for card in case['1st_row']:
        if (card in case['2nd_row']):
            if result == 0:
                result = card
            else:
                return "Bad magician!"
    if (result == 0):
        return "Volunteer cheated!" 
    else:
        return str(result)


# Main program
fin = open("A-small-attempt0.in")
numcases = int(fin.readline())
for casenum in range(1, numcases + 1):
    case_info = {}
    case_info['1st_selected_row'] = int(fin.readline())
    for row in range(1, 5):
        row_str = fin.readline()
        if (row == case_info['1st_selected_row']):
            case_info['1st_row'] = [int(x) for x in row_str.split()]
    
    case_info['2nd_selected_row'] = int(fin.readline())
    for row in range(1, 5):
        row_str = fin.readline()
        if (row == case_info['2nd_selected_row']):
            case_info['2nd_row'] = [int(x) for x in row_str.split()]
    
    print "Case #%d: %s" % (casenum, solve(case_info))
