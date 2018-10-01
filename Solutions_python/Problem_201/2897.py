input_file = open("C-small.in", "r")
output_file = open("output.txt", 'w')
total_cases = int(input_file.readline())

def recur(n):

    divs = []

    if n%2 == 0:

        divs.append(int((n/2)))
        divs.append(int((n/2)-1))

    else:

        divs.append(int((n-1)/2))
        divs.append(int((n-1)/2))

    return divs

for case in range(1, total_cases+1):

    line = input_file.readline().split()
    n = int(line[0])
    k = int(line[1])
    sideline = []
    result = []

    while k > 0:

        result = recur(n)
        n = max(result[0], result[1])
        sideline.append(min(result[0], result[1]))
        sideline = sorted(sideline)
        if n < sideline[-1]:
            plac = n
            n = sideline.pop()
            sideline.append(plac)
        k -= 1

    print(result)
    output_file.write("Case #" + str(case) + ": " + str(result[0]) + " " + str(result[1]) + "\n")


output_file.close()
