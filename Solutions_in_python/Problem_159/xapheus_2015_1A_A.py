__author__ = 'Xapheus'
# Python 3.4.3

# New to Python

f = open("A-large.in", 'r')
o = open("output_A.txt", 'w')
num_cases = int(f.readline())

for case in range(num_cases):
    num_measurements = f.readline()
    measurements = list(map(int, f.readline().split(' ')))
    comp1 = 0
    comp2 = 0
    max_drop = 0

    prev_i = 0
    for i in measurements:
        if i < prev_i:
            comp1 += prev_i - i
            if prev_i - i > max_drop:
                max_drop = prev_i - i
        prev_i = i

    for i in measurements[0:-1]:
        if i < max_drop:
            comp2 += i
        else:
            comp2 += max_drop
    print(case)
    o.write("Case #" + str(case + 1) + ": " + str(comp1) + " " + str(comp2) + "\n")

f.close()
o.close()