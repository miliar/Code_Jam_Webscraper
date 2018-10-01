__author__ = 'vladimir'

if __name__ == "__main__":
    inp = open("B-large.in")
    output = open("output.txt", 'w+')

    t = int(inp.readline())
    for i in range(0, t):
        s = inp.readline().strip()
        l = len(s)
        b = 0
        for ch in s:
            temp = 1 if ch == '+' else 0
            b <<= 1
            b += temp

        operations = 0
        counter = l - 1
        while counter >= 0:
            ones = True
            some_ones = False
            while ones and counter >= 0:
                b_temp = (b >> counter) & 1
                if b_temp == 1:
                    some_ones = True
                    counter -= 1
                else:
                    ones = False

            if ones:
                break

            while not ones and counter >= 0:
                b_temp = (b >> counter) & 1
                if b_temp == 1:
                    ones = True
                else:
                    counter -= 1

            operations += 1
            if some_ones:
                operations += 1

        output.write("Case #{0}: {1}\n".format(i + 1, operations))

    inp.close()
    output.close()
