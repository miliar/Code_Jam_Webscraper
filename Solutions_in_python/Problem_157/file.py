

def solve_problem(file_name):
    input_file = file_name + ".in"
    output_file = file_name + ".out"
    f = open(input_file, "r")
    g = open(output_file, "w")

    # Get test cases:
    
    test_cases = int(f.readline())
    for test_case in range(1, test_cases + 1):
        length, repeats = map(int, f.readline().split())
        string = f.readline().split()[0]
        answer = solve_test_case(string, repeats)
        result = "Case #" + str(test_case) + ": " + str(answer) + "\n"
        g.write(result)
        print result

    return "Done"
    
def solve_test_case(string, repeats):

    # make sure you have more than one letter
    letters_found = []
    for idx in range(len(string)):
        char = string[idx: idx+1]
        if char not in letters_found:
            letters_found.append(char)
        if len(letters_found) > 1:
            break
    if len(letters_found) < 2:
        return "NO"
    string = string * repeats
    
    string_length = len(string)

    # Make sure you can even make ijk = -1 with it all first.
    if multiply_quaternions(string) != "-1":
        return "NO"
    
    # Look for all possible left substrings
    for left_end in range(1, string_length - 1):
        s_left = string[0: left_end]
        not_s_left = string[left_end:]

        # To optimize algorithm, we only continue the search
        # if left product = i and everything else = jk = i
        left_prod = multiply_quaternions(s_left)
        if left_prod == "i" and multiply_quaternions(not_s_left) == "i":

            # Do the same for the middle substrings
            for mid_end in range(left_end + 1, string_length):
                s_mid = string[left_end: mid_end]
                # Same optimization!

                mid_prod = multiply_quaternions(s_mid)
                if mid_prod == "j":
                    
                    # Time to check if the search adds up.
                    s_end = string[mid_end: string_length]
                    end_prod = multiply_quaternions(s_end)
                    if end_prod == "k":
                        return "YES"
    return "NO"
    

def multiply_quaternions(string):
    # Start by building the multiplication table.
    multiply = {"1": {"1": "1", "i":  "i", "j":  "j", "k":  "k"},
                "i": {"1": "i", "i": "-1", "j":  "k", "k": "-j"},
                "j": {"1": "j", "i": "-k", "j": "-1", "k":  "i"},
                "k": {"1": "k", "i":  "j", "j": "-i", "k": "-1"}}
    
    product = string[0: 1]
    sign = "Positive"
    
    for char_idx in range(1, len(string)):
        
        multiplier = string[char_idx: char_idx + 1]
        
        product = multiply[product][multiplier]
        if product[0: 1] == "-":
            if sign == "Positive":
                sign = "Negative"
            else:
                sign = "Positive"
            product = product[1:]

    if sign == "Positive":
        return product
    else:
        return "-" + product

print solve_problem("C-small-attempt1")
