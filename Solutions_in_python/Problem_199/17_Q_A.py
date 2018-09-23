def main(file_in, file_out):
    lines = file_in.readlines()[1::]
    rows = [getInts(line.strip()) for line in lines]
    writeSolution(file_out, [solve(K,C,S) for K, C, S in rows])

def solve(K, C, S):
    if C == 1 or K == 1: result = range(1, K+1)
    else: result = range(2, K+1)

    print((K,C,S), "=>", result)

    if len(result) > S: return "IMPOSSIBLE"
    return ' '.join([str(n) for n in result])
        
def writeSolution(file, slns):
    lines = ["Case #{}: {}".format(n+1, slns[n]) for n in range(len(slns))]
    file_out.write('\n'.join(lines))

def getInt(line):
    return int(line.strip())

def getInts(line):
    return [int(token.strip()) for token in line.split()]

if __name__ == "__main__":
    with open("test.in", "r") as file_in, open("test.out", "w") as file_out:
            main(file_in, file_out)
            file_out.close()