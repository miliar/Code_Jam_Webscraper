input_file = open("B-small.in", "r")
output_file = open("output.txt", 'w')
total_cases = int(input_file.readline())

for case in range(1, total_cases+1):

    n = int(input_file.readline())
    last_perf_num = 1

    for i in range(1, n+1):

        num = [int(x) for x in list(str(i))]

        if sorted(num) == num:
            last_perf_num = i
            
    output_file.write("Case #" + str(case) + ": " + str(last_perf_num) + "\n")

output_file.close()
