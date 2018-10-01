def is_homo(l, j):
    if len(list(set(l))) == 1:
        if list(set(l)) == [j]:
            return True
    if len(sorted(list(set(l)))) == 2:
        if 0 in l:
            if j in l:
                return True
    return False

def get_all_i(m):
    result = set([])
    for i in m:
        for j in i:
            result.add(j)
            
    return sorted(list(result))

def transpose(m):
    result = [[[] for j in range(len(m))] for i in range(len(m[0]))]
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            result[j][i] = m[i][j]
    return result

def delete_row(m, r):
    result = []
    for i in range(len(m)):
        if i == r:
            l = [0 for j in range(len(m[i]))]
        else:
            l = [j for j in m[i]]
        result.append(l)
    return result

def is_possible(m):
    for i in m:
        for j in i:
            if j != 0:
                return False
    return True

def solution(parsed_line):
    m = [[int(j) for j in i.split(' ')] for i in parsed_line]

    all_i = get_all_i(m)
    
    for j in all_i:
        new_m = transpose(m)
        
        for r in range(len(new_m)):
            if is_homo(new_m[r], j):
                new_m = delete_row(new_m, r)
        new_m = transpose(new_m)

        for r in range(len(new_m)):
            if is_homo(new_m[r], j):
                new_m = delete_row(new_m, r)
        if m == new_m:
            break
        m = transpose(new_m)

    if is_possible(new_m):
        return 'YES'
    return 'NO'
    
def parse_input(f):
    data = open(f).read().split("\n")[:-1]
    result = []
    T = int(data[0])

    i = 1
    while i < len(data):
        N = int(data[i].split(' ')[0])
        M = data[i].split(' ')[1]
        q = []
        for j in range(i + 1, i + N + 1):
            q.append(data[j])
        i += N + 1
        result.append(q)
    return result

def solve():
    process_output = lambda l: l

    f = 'B-large.in'
    fout = open('output.txt', 'w')
    parsed_input = parse_input(f)

    for line in range(len(parsed_input)):
        s = "Case #" + str(line + 1) + ": " + process_output(solution(parsed_input[line])) + "\n"
        fout.write(s)

    fout.close()
    
solve()
