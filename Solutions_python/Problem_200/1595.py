import sys

def tidy_count(N):
    number_of_digits = len(str(N))
    if number_of_digits == 1:
        return N
    else:
        total_count = 0
        count_table = [[0 for j in range(1,10)] for i in range(0,number_of_digits)]
        count_table[0] = [1,1,1,1,1,1,1,1,1]
        total_count += sum(count_table[0])
        for i in range(1, number_of_digits):
            for j in range(0, 9):
                count_table[i][j] = sum(count_table[i-1][j:])
            if i == number_of_digits-1:
                number_as_string = str(N)
                len_ind = i
                prev_number = 0
                N_tidy_bool = True
                for d in number_as_string:
                    val = sum(count_table[len_ind][prev_number:int(d)-1])
                    total_count += val
                    if prev_number > int(d):
                        N_tidy_bool = False
                    prev_number = int(d) - 1
                    len_ind -= 1
                if N_tidy_bool:
                    total_count += 1
            else:
                total_count += sum(count_table[i])
        return total_count

def tidy_lowest(N):
    reversed = str(N)[::-1]
    num_arr = []
    for r in reversed:
        num_arr.append(int(r))
    prev_num = 9
    for ind, n in enumerate(num_arr):
        if prev_num < n:
            for j in range(0,ind):
                num_arr[j] = 9
            num_arr[ind] -= 1
        prev_num = num_arr[ind]
    string_return = ''
    for n in num_arr:
        string_return += str(n)
    return int(string_return[::-1])

f = open(sys.argv[1], 'r')
input_file = f.read().splitlines()
f.close()
output_file = open('output_large_tidy_numbers.out', 'w')
t = int(input_file[0])
for i in xrange(1, t + 1):
  n = input_file[i]
  output = tidy_lowest(int(n))
  out_string = "Case #" + str(i) + ": " + str(output)
  print out_string
  output_file.write(out_string)
  output_file.write('\n')

# print tidy_lowest(65)