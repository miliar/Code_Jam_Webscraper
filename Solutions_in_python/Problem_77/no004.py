with open('D-large.in', 'r') as fh:
    data = [row for row in fh.read().split('\n') if row]

cases = int(data[0])

result = ''
for case in range(1, cases + 1):
    num_values = int(data[2*case - 1])
    row = [int(val) for val in data[2*case].split() if val]
    if len(row) != num_values:
        raise Exception("Bad data")

    count_incorrect = num_values
    for index in range(num_values):
        if row[index] == index + 1:
            count_incorrect -= 1
    print 'Case #%s: %s.000000' % (case, count_incorrect)
    result += 'Case #%s: %s.000000\n' % (case, count_incorrect)

result = result.strip()

with open('D-large.out', 'w') as fh:
    fh.write(result)
