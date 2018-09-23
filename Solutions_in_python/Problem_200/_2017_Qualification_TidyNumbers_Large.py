with open('B-large.in','r') as input:
    
    file = input.read().split("\n")

    #Number of cases T
    T = int(file[0])

    #Storing results as a list for easier output
    results_list = list()

    current_line = 1

    for case in range(1,T+1):

        N = file[current_line]

        #Break the number into digits
        digits = [int(x_temp) for x_temp in N]

        last_tidy_number = ""

        current_digit = len(digits)-1

        while current_digit >=1:
            previous_digit = current_digit - 1
            
            if digits[current_digit] >= digits[previous_digit]:
                current_digit -=1
                continue
                
            else:
                digits[previous_digit] -= 1

                #Make all digits after the changed one be 9's
                for index in range(current_digit,len(digits)):
                    digits[index] = 9

                current_digit -=1

        #Remove leading zeros
        non_zero_index = 0
        while non_zero_index < len(digits):
            if digits[non_zero_index] != 0:
                break
            non_zero_index +=1

        for digit in digits[non_zero_index:]:
            last_tidy_number += str(digit)



        results_list.append((str(case),str(last_tidy_number)))

        current_line+=1

with open('B-large.out','w') as output:
    for case in results_list:
        output.write("Case #" + case[0] + ": " + case[1] + "\n")