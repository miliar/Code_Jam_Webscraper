
def read_file(filename: str):
    cases = []
    with open(filename) as f:
        T = int(f.readline().strip())
        for t in range(T):
            line = f.readline().split()
            N = int(line[0])
            K = int(line[1])
            cases.append({'N': N, 'K': K})
    return cases

