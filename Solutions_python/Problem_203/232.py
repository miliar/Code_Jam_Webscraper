"""
Google Code Jam, Problem ?
"""

def solve(matrix):
    """
    solve problem
    """

    # fill rows left to right

    for row in matrix:
        #complete the left most cell if possible
        if row[0] == '?':
            for e in row:
                if e != '?':
                    row[0] = e
                    break

    for row in matrix:
        #complete rows if the left most cell is not a '?'
        if row[0] != '?':
            for i in range(1, len(row)):
                if row[i] == '?':
                    row[i] = row[i-1]

    if matrix[0][0] == '?':
        for row in matrix:
            if row[0] != '?':
                break
        matrix[0] = row

    for i in range(1, len(matrix)):
        if matrix[i][0] == '?':
            matrix[i] = matrix[i-1]

    return matrix


def main():
    """
    main function
    """
    cases = int(input())
    for i in range(0, cases):
        dim = list(map(int, input().split(' '))) # [rows, cols]
        matrix = []
        for _ in range(dim[0]):
            matrix.append(list(input()))
        result = solve(matrix)

        print("Case #" + str(i+1) + ":")
        for row in result:
            print("".join(row))

if __name__ == '__main__':
    main()
