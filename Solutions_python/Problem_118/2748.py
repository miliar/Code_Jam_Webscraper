import sys

def is_square(number):
    n = 1 
    while n * n < number:
        if n * n == number:
            break
        n += 1
    if n * n == number:
        return (True, n)
    else:
        return (False, 0)

def is_panlindrome(string):
    n = len(string)
    if n == 1:
        return True
    half_n = n/2
    for i in range(half_n):
        if string[i] != string[n-1-i]:
            return False
    return True

def is_square_palindrome(number):
    (is_sq, sqrt) = is_square(number)
    is_sqrt_palindrome = is_panlindrome(str(sqrt))
    is_palin = is_panlindrome(str(number))
    return ((is_palin & is_sq )& is_sqrt_palindrome)

if __name__ == "__main__":
    file_name = str(sys.argv[1])
    f = open (file_name, "r")

    # Step 1 - Read the number of datasets and set counter for data
    N = int(f.readline())
    counter = 0

    output_file = open("fair_n_square.out", "w")


    # Iterate through all data
    while counter < N:
        counter += 1
        output_line = "Case #" + str(counter) + ": "
        line = (f.readline())
        n_range = (line.strip('\n')).split()
        low = int(n_range[0])
        high = int(n_range[1])

        fs_count = 0
        for number in range(low, high+1):
            # print number
            # print str(number)
            if is_square_palindrome(number):
                # print str(number) + ' is fair and square'
                fs_count += 1

        output_line += str(fs_count)
        print(output_line)
      	output_file.write(output_line + "\n")

    f.close()
    output_file.close()
