cases = int(input(""))

for case in range(cases):
    (max_shyness, encoded) = input("").split(' ')
    max_shyness = int(max_shyness)
    encoded = [int(x) for x in list(encoded)]

    to_add = 0
    total = 0
    for i in range(0,len(encoded)):
        if (total < i):
            to_add += i - total
            total = i
        total += encoded[i]

    print("Case #{}: {}".format(case + 1, to_add))