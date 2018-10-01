import numpy as np

# Input
file = "B-large.in"
text = [line.rstrip() for line in open(file, 'r')]
cases = text[0]
values = text[1:]

# Functions
def istidy(num):
    num_str = str(int(num))
    check = [(num_str[i]) <= (num_str[i+1]) for i in range(len(num_str)-1)]
    return all(check), check

def prevtidy(num):
    tidy, check = istidy(num)
    while not tidy:
        first = min([i for i in range(len(check)) if not check[i]])
        num -= int(str(num)[first+1:]) + 1
        tidy, check = istidy(num)
    return num

# Get result
results = []
for n in values:
    results.append(prevtidy(int(n)))
print(results)

# Verify
for num in results:
    if not istidy(num):
        raise ValueError("Not tidy!")

file = open("output.txt", 'w')
for i in range(len(results)):
    file.write("Case #{:d}: {:d}\n".format(i+1, results[i]))