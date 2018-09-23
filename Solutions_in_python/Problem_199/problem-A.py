def flip(row, beg_pos, k):
    flipped_row = ''
    for i in range(beg_pos, beg_pos+k):
        flipped_row += '+' if row[i] == '-' else '-'
    return row[:beg_pos] + flipped_row + row[beg_pos+k:]

# print(flip('+--+-+', 2, 3))

in_file = 'A-large.in'
out_file = 'A-large.out'
inp = open(in_file, 'r')
out = open(out_file, 'w')

t = int(inp.readline())
for case in range(1, t+1):
    row, k = inp.readline().split()
    k = int(k)

    flip_count = 0
    while '-' in row[:-k]:
        pos = row.find('-')
        row = flip(row, pos, k)
        flip_count += 1
    if '-' in row[-k:] and '+' in row[-k:]:
        ans = 'IMPOSSIBLE'
    elif '-' in row[-k:]:
        ans = flip_count + 1
    else:
        ans = flip_count
    out.write('Case #{}: {}\n'.format(case, ans))

inp.close()
out.close()
