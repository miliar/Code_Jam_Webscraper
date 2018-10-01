


def backNine(row, i):
    for j in range(i, len(row)):
        row[j] = '9'
    return row

def dec(nb):
    return str((int(nb) + 9) % 10)

def algo(row, case):
    row = list(row)
    for i in range(len(row)-1, 0, -1):
        if int(row[i]) < int(row[i-1]):
            row[i-1] = dec(row[i-1])
            row = backNine(row, i)
    while (row[0] == '0'):
        row.pop(0)
    row = ''.join(row)
    print('Case #'+str(case)+':', row)


def main():
    n = int(input())
    for i in range(n):
        row = input()
        algo(row, i+1)

main()