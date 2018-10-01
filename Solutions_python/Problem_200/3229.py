#!/usr/bin/python3
#SETTINGS:
SINGLE_INT_PER_ROW = True



nr_of_tasks = int(input())
result = ""

def check_strict_inc(tser):
    for i in range(1,len(tser)):
        if not tser[i] >= tser[i-1]:
            return i
    return 0


def task_calc(task_data):
    value = str(task_data)
    new_value=[0]*len(value)
    #Check if increasing series of integers.

    break_pos = check_strict_inc(value)
    if break_pos==0:
        return value

    for i in range(break_pos, len(value)):
        new_value[i]=9

    mem=1
    for i in range(break_pos-1, 0, -1):
        val = int(value[i])
        if mem == 1:
            val = (val - 1) % 10
            mem = 0
        while True:
            if val == 9:
                mem = 1

            if val >= int(value[i-1]):
                new_value[i]= val
                break
            else:
                val = (val-1) % 10
    if mem==1:
        val=int(value[0])-1
        new_value[0]=val
    else:
        new_value[0]=int(value[0])

    if not (check_strict_inc("".join([str(a) for a in new_value]))) == 0:
        print("ERROR")
        print(new_value)
        print(value)
        exit(1)

    if new_value[0]==0:
        del new_value[0]

    return "".join([str(a) for a in new_value])


for task_index in range(0,nr_of_tasks):
    if SINGLE_INT_PER_ROW:
        inrow = int(input())
    else:
        inrow = [int(a) for a in str(input()).split(" ")]
    result = task_calc(inrow)
    print("Case #{task}: {result}".format(task=task_index+1,
                                 result=str(result)))