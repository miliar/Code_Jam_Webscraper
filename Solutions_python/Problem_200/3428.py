#!/usr/bin/python


#-----------------------------------------------------
# check the input number is tidy by comparing each
# digit to it predecessor and making sure its larger

def isTidy(string):
    number_of_digits = len(string)
    last_digit = -1
    for digit in string:
        digit_int = int(digit)
        if(digit_int < last_digit):
            return False
        last_digit = digit_int
    return True

#-----------------------------------------------------
# recursive function to make a number tidy

def recurse( counter, no, tno):
    length = len(tno)
    # if it's tidy and less than the input number,
    # nothing to do
    if( isTidy(tno) and int(tno) <= int(no) ):
        return tno

    # if the proposed tidy number is larger than
    # the input number, we need to reduce the number
    # to the left of the number we changed last time
    # by 1, unless it happens to be 1, in which case
    # we change it to 9 (or 0, is it's the first digit)
    
    if( int(tno) > int(no) ):
        index_tochange = counter-2
        dig = int(tno[index_tochange])
        if(dig == 1 and index_tochange!= 0):
            dig = 9
        else:
            dig = dig -1
        tno = tno[:index_tochange] + str(dig) + tno[index_tochange+1:]
        tno = tno.strip('0')
        if( int(tno) > int(no) ):
            # if the tidy number is still larger, the next left
            # digit needs adjusting. Make sure the counter is
            # set to get things righ the next time around
            counter = counter-1
        else:
            # If the number is now smaller, let's start over and
            # make sure it's still tidy
            counter = 1
        return recurse(counter, no, tno)
    if(tno[counter] < tno[counter-1]):
        # set this digit, and all subsequent ones to 9
        for i in range(counter, length):
            tno = tno[:i] + "9" + tno[i+1:]
    counter = counter + 1
    return recurse(counter, no, tno)
    

#-----------------------------------------------------
    
fin = open("tidy_number_sample.txt", "r")
number_of_test_cases = int(fin.readline()) ;
print("Number of test cases: ", number_of_test_cases)

fout = open('tidy_number_output.txt', 'w')

for x in range(0, number_of_test_cases):
    string = fin.readline().rstrip('\n')
    print("input: ", string, "input length ", len(string))
    
    tidynumber = recurse(1, string, string)

    output_string = 'Case #' + str(x+1) + ": " + str(tidynumber) + "\n" 
    print("length of tidy number", len(tidynumber))
    print(output_string)
    fout.write(output_string)
    
fout.close()
fin.close()

