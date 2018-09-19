def traverse(root, path):
    mkdir = 0
    p = path.pop(0)
    if p not in root:
        root[p] = {}
        mkdir += 1
    if len(path) > 0:
        mkdir += traverse(root[p], path)
    return mkdir

def solve(m, n, ex, nu):
    root = {}
    mkdir = 0
    for l in ex:
        traverse(root, l.split('/')[1:])
#    print('Current filesystem:', root)
    for l in nu:
        mkdir += traverse(root, l.split('/')[1:])
#    print('New filesystem:', root)
    return mkdir

def split(line):
    return line.replace('\n', '').split(' ')

if __name__ == '__main__':

    input_problem = 'A'
    input_set = 'large'#-attempt0'
    in_file = open('{}-{}.in'.format(input_problem, input_set), 'r')
    out_file = open('{}-{}.out'.format(input_problem, input_set), 'w')

    line = in_file.readline()

    count = int(line)
    for i in range(1, count+1):
        print(i, 'of', count)
        m, n = split(in_file.readline())
        m, n = int(m), int(n)
        ex, nu = [], []
        for j in range(m):
            ex.append(in_file.readline().replace('\n', ''))
        for j in range(n):
            nu.append(in_file.readline().replace('\n', ''))
        out_file.write('Case #{}: {}\n'.format(i, solve(m, n, ex, nu)))

    in_file.close()
    out_file.close()

