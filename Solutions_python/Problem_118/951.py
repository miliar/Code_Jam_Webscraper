#!/usr/bin/python
import math
import sys

fair_square_list = []

def next_palindrome(palindrom_as_list):
    start_list = palindrom_as_list[:] # copy to avoid mutating original list
    length = len(start_list)
    cascade = False # means there is more work to be done, ie 191 -> 202 (the carry over)

    # special case
    if palindrom_as_list == [9]:
        return [1,1]

    if length %2 is 1:
        # if the length is odd, increment the middle one
        mid = length / 2

        start_list[mid] = (start_list[mid] + 1) %10

        if start_list[mid] is 0:
            # carry the digits both directions
            cascade = True
            mid_1 = mid + 1
            mid_0 = mid - 1

    else:
        # if the length is even
        mid_1 = length / 2
        mid_0 = mid_1 - 1
        cascade = True

    if cascade:
        # loop until we we either stop carrying digits or we reach the bounds of the list
        while ((start_list[mid_1] == 0 and start_list[mid_0] == 0) or (start_list[mid_1] and start_list[mid_0])):
            start_list[mid_1] = (start_list[mid_1] + 1) %10
            start_list[mid_0] = (start_list[mid_0] + 1) %10

            if (start_list[mid_1] is 0):
                # carry over, change our indecies
                mid_1 += 1
                mid_0 -= 1

                if mid_1 >= length:
                    # if we hit the bounds of the list, we need a bigger list [1.......1]
                    start_list.insert(0, 1) # insert '1' at the beginning
                    start_list[-1] = 1 # modify the last element
                    length += 1 # update the length
                    break


            else:
                # no carry over, done
                break

    return start_list

def is_palindrome(string):
    for i in range(len(string)/2):
        end = len(string) - 1
        if string[i] != string[end - i]:
            return False
    return True

def get_fair_squares(start, end):
    count = 0
    for i in fair_square_list:
        if int(start) <= int(i) <= int(end):
            count += 1
        if int(i) > int(end):
            break
    return count

# use the above function to find palindromes as lists of integers
def make_fair_squares():
    palindrome  = [1]
    #fair_square_list = []

    while 1 <= int(''.join(str(x) for x in palindrome)) <= 100000000000000:
        sqrt = math.sqrt(int(''.join(str(x) for x in palindrome)))
        after_decimal = sqrt %1
        if not after_decimal:
            sqrt = int(sqrt)
        if isinstance(sqrt, int) and is_palindrome(str(sqrt)):
            fair_square_list.append(''.join(str(x) for x in palindrome))
        palindrome = next_palindrome(palindrome)

    #return fair_square_list


try:
    source_file = open(sys.argv[1], 'r')
except:
    print "Error opening file"
    sys.exit()

line = source_file.readline()
total_cases = int(line)


# populate a list of fair squares
make_fair_squares()

#print fair_square_list

# read file
i = 0
while 1:
    line = source_file.readline()
    if not line:
        break

    i += 1
    bounds_string = line
    bounds_list = line.split()

    result_count = get_fair_squares(bounds_list[0], bounds_list[1])

    print "Case #%s: %s" % (i, result_count)

