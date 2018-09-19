def parse_line(line):
    values = line.split()
    num_combinations = int(values[0])
    base_index = 1
    combine_hash = {}
    for value in values[base_index:num_combinations + base_index]:
        first, second, new = value
        if first in combine_hash:
            combine_hash[first][second] = new
        else:
            combine_hash[first] = {second: new}
        if second in combine_hash:
            combine_hash[second][first] = new
        else:
            combine_hash[second] = {first: new}

    num_opposed = int(values[num_combinations + base_index])
    base_index = num_combinations + base_index + 1
    opposed_hash = {}
    for value in values[base_index:num_opposed + base_index]:
        first, second = value
        if first in opposed_hash:
            opposed_hash[first][second] = 1
        else:
            opposed_hash[first] = {second: 1}
        if second in opposed_hash:
            opposed_hash[second][first] = 1
        else:
            opposed_hash[second] = {first: 1}

    num_invoke = int(values[-2])
    invoke_string = values[-1]

    return combine_hash, opposed_hash, invoke_string

def final_list(line):
    combine_hash, opposed_hash, invoke_string = parse_line(line)

    result = []
    for element in invoke_string:
        if result == []:
            result.append(element)
        else:
            last = result[-1]
            if last in combine_hash and element in combine_hash[last]:
                combined_elt = combine_hash[last][element]
                result = result[:-1] + [combined_elt]

            elif (element in opposed_hash and
                  set(opposed_hash[element]).intersection(result)):
                result = []
            else:
                result.append(element)

    return result

with open('B-large.in', 'r') as fh:
    data = fh.read()

lines = [row for row in data.split('\n') if row]
cases = int(lines[0])

result = ''
for problem in range(1, cases + 1):
    final_elt_list = final_list(lines[problem])
    pretty_list = '[' + ', '.join(final_elt_list) + ']'
    print 'Case #%s: %s' % (problem, pretty_list)
    result += 'Case #%s: %s\n' % (problem, pretty_list)

result = result.strip() # trailing newline

with open('B-large.out', 'w') as fh:
    fh.write(result)
