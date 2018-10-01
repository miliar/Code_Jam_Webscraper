import struct, fractions

#input read
input_file = open("input1.in", 'rt')
num_cases = int(input_file.readline())

#output write
output_file = open("output1.txt", 'w')


# do the job
def main_job(files, capacity):
    count = 0
    files.sort()
    while len(files) > 0:
        if len(files) == 1:
            count += 1
            break

        if files[-1] + files[0] <= capacity:
            files.pop(0)
        files.pop(-1)
        count += 1

    return count

for i in range(num_cases):
    print i
    line = input_file.readline()
    line = line.split()
    num_files = int(line[0])
    capacity = int(line[1])

    line = input_file.readline()
    files = map(int, line.split())

    result = main_job(files, capacity)

    output = "Case #%d: %d\n" %(i+1, result)

    output_file.write(output)

input_file.close()
output_file.close()