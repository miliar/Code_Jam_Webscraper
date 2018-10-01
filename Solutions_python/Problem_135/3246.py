import sys
curr_case = 1
input_list = sys.stdin.readlines()
max_case = int(input_list[0])
input_list.pop(0)

def getRow(list):
    row_num = int(list[0])
    row = list[row_num].split()
    return row

def getCommonCards(list1, list2):
        return_list = []
        for i in list1:
            if i in list2:
                return_list.append(i)
        return return_list

while (curr_case <= max_case):
    row1 = getRow(input_list)
    input_list = input_list[5:]
    row2 = getRow(input_list)
    input_list = input_list[5:]
    common_cards = getCommonCards(row1, row2) 
    if len(common_cards) == 1:
        print "Case #%s:" % (curr_case), common_cards[0]
    elif len(common_cards) == 0:
        print "Case #%s:" % (curr_case), "Volunteer cheated!"
    else:
        print "Case #%s:" % (curr_case), "Bad magician!"
    curr_case = curr_case + 1
        
