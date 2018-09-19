inp = input("Enter the file name: ")
op = open(inp,'r')
file = op.read().split("\n")
T = eval(file[0])
      
def quickSortHelper(lst, first, last):
    pivot = lst[first]
    low = first + 1
    high = last
    while high > low:
        while low <= high and lst[low] <= pivot:
            low += 1

        while low <= high and lst[high] > pivot:
            high -= 1

        if high > low:
            lst[high], lst[low] = lst[low], lst[high]

    while high > first and lst[high] >= pivot:
        high -= 1

    if pivot > lst[high]:
        lst[first] = lst[high]
        lst[high] = pivot
        return high
    else:
        return first     
        

def quickSort(lst, first, last):
    if last>first:
        pivotIndex = quickSortHelper(lst, first, last)
        quickSort(lst, first, pivotIndex -1)
        quickSort(lst, pivotIndex + 1, last)
temp = 2
for i in range(T):
    lst = file[temp].split()
    
    total = eval(file[temp - 1])
    first = eval(lst[0])
    if total == 1:
        if first <=3:
            answer = eval(lst[0])
        elif first == 4 or first == 5:
            answer = first - 1
        elif first == 6 or first == 7:
            answer = first - 2
        else:
            answer = 5
    else:
        ls = []
        for hmm in lst:
            ls.append(eval(hmm))
        quickSort(ls, 0, len(ls)-1)
        ls.reverse()

        if ls[0] <= 3:
            answer = ls[0]
        
        elif ls[0] == 4 or ls[0] == 5:
            if ls[1] >= 3 and ls[0] == 4:
                answer = 4
            elif ls[1] >= 4 and ls[0] == 5:
                answer = 5
            else:
                if ls[0] == 4:
                    answer = 3
                else:
                    answer = 4
        elif ls[0] == 6 or ls[0] == 7:
            if len(ls) > 2 and (ls[0] == ls[1] == 6):
                if ls[2] > 3:
                    answer = 6
                else:
                    answer = 5
            elif len(ls) > 2 and (ls[0] == ls[1] == 7):
                if ls[2] > 4:
                    answer = 7
                else:
                    answer = 6
            elif ls[1] >= 4 and ls[0] == 6:
                if len(ls) > 2 and (ls[1] == 5 or ls[1] == 6) and (ls[2] == 5 or ls[2] == 6 or ls[2] == 4):
                    answer = 6
                else:
                    answer = 5
            elif ls[1] >= 5 and ls[0] == 7:
                if len(ls) > 2 and (ls[1] == 6 or ls[1] == 7) and (ls[2] == 6 or ls[2] == 7 or ls[2] == 5):
                    answer = 7
                else:
                    answer = 6
            else:
                if ls[0] == 6:
                    answer = 4
                else:
                    answer = 5

        elif ls[0] == 8 or ls[0] == 9:
            if len(ls) > 3 and (ls[0] == ls[1] == ls[2] == 8):
                if ls[3] > 4:
                    answer = 8
                else:
                    answer = 7
            elif len(ls) > 3 and (ls[0] == ls[1] == ls[2] == 9):
                if ls[3] > 5:
                    answer = 9
                else:
                    answer = 8
            elif len(ls) > 2 and (ls[0] == ls[1] == 8):
                if ls[2] > 4:
                    if len(ls) > 3 and (ls[2] == 6 or ls[2] == 7) and ls[3] >= 5:
                        answer = 8
                    else:
                        answer = 7
                else:
                    answer = 6
            elif len(ls) > 2 and (ls[0] == ls[1] == 9):
                if ls[2] > 5:
                    if len(ls) > 3 and (ls[2] == 7 or ls[2] == 8) and ls[3] >= 6:
                        answer = 9
                    else:
                        answer = 8
                    
                else:
                    answer = 7
            elif ls[1] > 4 and ls[0] == 8:
                if len(ls) > 2 and ls[1] == 6 and (ls[2] == 5 or ls[2] == 6):
                    if len(ls) > 3 and ls[3] > 5 and ls[2] == 6:
                        answer = 8
                    else:
                        answer = 7
                elif len(ls) > 2 and ls[1] == 7 and ls[2] >= 5:
                    if len(ls) > 3 and ls[3] > 5 and (ls[2] == 6 or ls[2] == 7):
                        answer = 8
                    else:
                        answer = 7
                else:
                    answer = 6
            elif ls[1] > 6 and ls[0] == 9:
                if len(ls) > 2 and (ls[1] == 7 or ls[1] == 8) and (ls[2] > 5):
                    if len(ls)>3 and ls[3] > 5 and ls[1] == 8:
                        answer = 9
                    else:
                        answer = 8
                else:
                    answer = 7
                
            elif 3 < ls[1] < 7 and ls[0] == 9:
                if len(ls) > 2 and ls[1] == 6 and (ls[2] == 5 or ls[2] == 6):
                    if len(ls) > 3 and ls[2] == 6 and ls[3] == 6:
                        if len(ls) > 4 and ls[4] == 6:
                            answer = 9
                        else:
                            answer = 8
                    else:
                        answer = 7
                else:
                    answer = 6
            else:
                answer = 5
    print("Case #" + str(i+1) + ": " + str(answer))
    temp += 2































    
    
