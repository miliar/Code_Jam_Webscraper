import sys

def change(my_input):
    my_string = str(my_input)
    my_length = len(my_string)
    return_string = ""

    for i in range(my_length):
        if (my_string[i] == 'a'):
            return_string += 'y'
        elif (my_string[i] == 'b'):
            return_string += 'h'
        elif (my_string[i] == 'c'):
            return_string += 'e'
        elif (my_string[i] == 'd'):
            return_string += 's'
        elif (my_string[i] == 'e'):
            return_string += 'o'
        elif (my_string[i] == 'f'):
            return_string += 'c'
        elif (my_string[i] == 'g'):
            return_string += 'v'
        elif (my_string[i] == 'h'):
            return_string += 'x'     
        elif (my_string[i] == 'i'):
            return_string += 'd'
        elif (my_string[i] == 'j'):
            return_string += 'u'
        elif (my_string[i] == 'k'):
            return_string += 'i'
        elif (my_string[i] == 'l'):
            return_string += 'g'
        elif (my_string[i] == 'm'):
            return_string += 'l'
        elif (my_string[i] == 'n'):
            return_string += 'b'
        elif (my_string[i] == 'o'):
            return_string += 'k'
        elif (my_string[i] == 'p'):
            return_string += 'r'
        elif (my_string[i] == 'q'):
            return_string += 'z'
        elif (my_string[i] == 'r'):
            return_string += 't'
        elif (my_string[i] == 's'):
            return_string += 'n'
        elif (my_string[i] == 't'):
            return_string += 'w'
        elif (my_string[i] == 'u'):
            return_string += 'j'
        elif (my_string[i] == 'v'):
            return_string += 'p'
        elif (my_string[i] == 'w'):
            return_string += 'f'
        elif (my_string[i] == 'x'):
            return_string += 'm'
        elif (my_string[i] == 'y'):
            return_string += 'a'
        elif (my_string[i] == 'z'):
            return_string += 'q'
        elif (my_string[i] == ' '):
            return_string +=  ' '
        else:
            pass

    return return_string

if __name__ == "__main__":          
    f = open ("A-small-attempt2.in")
    output = open ("output", "w")

    lines = f.readlines()

    lines = [s.strip() for s in lines]

    my_number = int(lines.pop(0))

    for i in range(my_number):
        my_string = str(lines[i])
        my_string_2 = change(my_string)
        my_string_3 = "Case #" + str(i+1) + ": " + my_string_2 +"\n"
        print my_string_3
        output.write(my_string_3)
        
        
    
    
    
