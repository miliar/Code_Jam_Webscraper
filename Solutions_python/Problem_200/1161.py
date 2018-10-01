# !/bin/python3

import math

with open("pbb.input", "r") as input:
    with open("pbb.output", "w") as output:
        testCases = int(input.readline().strip())

        T = 0
        for line in input.readlines():
            T += 1
            data = [int(x) for x in line.strip()]

            firstIndex = 0
            for i in range(1, len(data)):
                if data[i] < data[i - 1]:
                    data[firstIndex + 1:] = [9] * (len(data) - (firstIndex + 1))
                    data[firstIndex] -= 1
                    break
                elif data[i] > data[i - 1]:
                    firstIndex = i
            output.write("Case #" + str(T) + ": " + str(int("".join([str(x) for x in data]))) + "\n")

        pass