#!/usr/bin/python
import sys

def get_min(arr):
    if len(arr) == 1:
        return 0

    for i,el in enumerate(arr):
        if el > i:
            ind = i
            break
    else:
        return 0

    next_ind = ind+1
    while arr[next_ind] > i:
        next_ind += 1

    new_arr = arr[:ind]+[arr[next_ind]]+arr[ind:next_ind]+arr[next_ind+1:]
    return get_min(new_arr) + next_ind-ind

    """
    biggest = None
    for i,el in enumerate(arr):
        if el==len(arr)-1:
            biggest = i

    if biggest is not None:
        new_arr = arr[:biggest] + arr[biggest+1:]
        return get_min(new_arr) + len(arr)-1-biggest

    else:
        return get_min(new_arr[1:]) + arr[0]
    """

def calc_ans(mat):
    arr = []
    for line in mat:
        last = -1
        for i,el in enumerate(line):
            if el == "1":
                last = i
        arr.append(last)
    return get_min(arr)

def main():
    handle = file(sys.argv[1])
    n = int(handle.readline())

    for case_no in range(1,n+1):
        N = int(handle.readline())
        mat = []
        for i in range(N):
            mat.append(list(handle.readline()[:-1]))

        print "Case #%d: %d" % (case_no, calc_ans(mat))

main()
