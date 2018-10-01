


def rec(acc, num_digits, n):
    end = -1
    if acc == 0:
        end = 0

    if num_digits == 0:
        return acc

    for digit in range(9, 0, -1):
        dlist = [digit for _ in range(num_digits)]
        idlist = sum(10 ** i * dlist[i] for i in range(num_digits))
        #print (acc, idlist)
        if acc + idlist <= n:
            return rec(acc + digit*10**(num_digits-1), num_digits - 1, n)

    return -1;

def solve(n):
    for digits in range(30, 0, -1):
        temp = rec(0, digits, n)
        if temp != -1:
            return temp

def main():
    f = open("test.in", "r")
    lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]

    T = int(lines[0])

    g = open("test.out", "w")
    for test_case in range(1, T+1):
        ans = solve(int(lines[test_case]))
        g.write("Case #" + str(test_case) + ": " + str(ans) + "\n")


main()
