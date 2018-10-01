""" Google Code Jam - Qualification
    Part B Solution
    Author: Marc Katzef
"""

    
def solution(in_file):
    """Uses the data in in_file to generate an answer as a single string to be written to file"""
    out_list = []
    
    test_cases = int(in_file.readline().strip())

    for i in range(test_cases):
        N = int(in_file.readline().strip())
        
        number_options = []
        for digit in str(N):
            digit_options = [j for j in range(int(digit) + 1)]
            number_options.append(digit_options)
        
        if len(number_options) == 1:
            test_number = [number_options[0][-1]]
            success = True
        else:
            success = False
            
        while (not success) and len(number_options) > 1:
            first_entry = number_options[0][-1]
            test_number = [first_entry]
            for j in range(1, len(number_options)):
                new_digit = number_options[j][-1] # could be 0
                if new_digit < test_number[-1]:
                    popped = number_options[j-1].pop()
                    if j == 1 and popped == 0:
                        number_options.pop(0)
                    else:
                        for k in range(j, len(number_options)):
                            number_options[k] = [l for l in range(10)]
                    break
                        
                else:
                    test_number.append(new_digit)
                    if j == len(number_options) - 1:
                        success = True
        
        result = int("".join(map(str, test_number)))
        out_line = "Case #%d: %d" %(i+1, result)
        out_list.append(out_line)
    
    return out_list
    

def main():
    """Opens the input file, collects the generated answer and writes it to the output file."""
    input_name = 'B-large.in'
    output_name = 'B\'s-output.txt'
    
    in_file = open(input_name)
    out_file = open(output_name, 'w')

    out_list = solution(in_file)
    out_string = '\n'.join(out_list)
    out_file.write(out_string)
    
    in_file.close()
    out_file.close()

    
main()

