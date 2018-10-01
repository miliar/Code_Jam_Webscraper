in_file = open("./A-large.in", 'r')
# in_file = open("./small_input.txt", 'r')
out_file = open("./output.txt", 'w')

inputs = in_file.read().strip().split("\n")

t_c = int(inputs.pop(0))

t = 0
while t < t_c:
    pancakes, flipper = inputs[t].split(" ")
    pancakes = list(pancakes)
    flipper = int(flipper)
    flips = 0

    l_s = len(pancakes)
    for l in range(l_s - flipper + 1):
        if pancakes[l] == "-":
            flips += 1
            for p in range(l, l + flipper):
                if pancakes[p] == "+":
                    pancakes[p] = "-"
                else:
                    pancakes[p] = "+"
            l += flipper

    if "-" in pancakes:
        out_file.write("Case #{}: IMPOSSIBLE\n".format(t + 1))
    else:
        out_file.write("Case #{}: {}\n".format(t + 1, flips))

    # print(pancakes, "\n", flips)

    t += 1
