import copy

def get_list_from_line(line):
    ls = filter(None, line.split(' '))
    for i in range(len(ls)):
        ls[i] = int(ls[i])        
    return ls

def get_max_from_row(row):
    max = 0
    for elem in row:
        if elem > max:
            max = elem
    return max

def get_max_from_col(n, col, desired):
    max = 0
    for i in range(n):
        if desired[i][col] > max:
            max = desired[i][col]
    return max

def mow_row(height, row, lawn):
    for j in range(len(lawn[row])):
        lawn[row][j] = height

def mow_every_column(n, m, lawn, desired):
    for j in range(m):
        max = get_max_from_col(n, j, desired)
        for i in range(n):
            if lawn[i][j] > max:
                lawn[i][j] = max

def get_NM(line):
    ls = get_list_from_line(line)
    return (ls[0], ls[1])

def make_lawn(n, m):
    lawn = []
    for i in range(n):
        ls = [100] * m
        lawn.append(ls)
    return lawn

def compare(desired, lawn, n, m):
    for i in range(n):
        for j in range(m):
            if desired[i][j] < lawn[i][j]:
                return 'NO'
    return 'YES'
    
def main():
    output = open('2.out', 'w')
    with open('B-large.in', 'r') as input:
        cases = int(input.readline().split('\n')[0])
        for case in range(cases):
            (n, m) = get_NM(input.readline().split('\n')[0])
            desired = []
            for i in range(n):
                desired.append(get_list_from_line(input.readline().split('\n')[0]))
            lawn = make_lawn(n, m)
            for i in range(n):
                max = get_max_from_row(desired[i])
                mow_row(max, i, lawn)
            mow_every_column(n, m, lawn, desired)
            status = compare(desired, lawn, n, m)
            toWrite = 'Case #{0}: {1}\n'.format(str(case + 1), status)
            output.write(toWrite) 

    output.close()

if __name__ == "__main__":
    main()
