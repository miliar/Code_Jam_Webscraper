def flipped(pancakes):
    return ['+' if pancake == '-' else '-' for pancake in pancakes]

def solve(table, size):
    table = list(table)
    moves = 0
    for i in range(max(1,len(table)-size)):
        print(*table, sep='')
        if table[i] == '-':
            table = (table[:i]
                + flipped(table[i:i+size])
                + table[i+size:])
            moves += 1
    for i in range(len(table)-1, max(len(table)-size-1, size-1), -1):
        print(*table, sep='')
        if table[i] == '-':
            i += 1
            table = (table[:i-size]
                + flipped(table[i-size:i])
                + table[i:])
            moves += 1
    print(*table, sep='')
    return (''.join(table), moves)

tests = []
for line in open('A-small-attempt1.in', 'r').readlines()[1:]:
    table, size = line.split()
    tests+= [(table, int(size))]

results = []
i = 0
for table, size in tests:
    print(table, size)
    final_table, moves = solve(table, size)
    if '-' in final_table: moves = 'IMPOSSIBLE'
    i += 1
    print(f'Case #{i}: {moves}')
    results += [f'Case #{i}: {moves}']

with open('out.txt', 'w') as results_file:
    for result in results:
        results_file.write(result+'\n')
