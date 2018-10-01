file = open("A-small-attempt0.in", "r")
filecontents = file.read()
file.close()

filecontents = filecontents.split("\n")
cases = int(filecontents[0])
filecontents = filecontents[1:(len(filecontents)-1)]

def solve(string):
    invite = 0
    standing = 0
    lst = list(string)
    numbers = [int(x) for x in lst]
    for i in range(len(numbers)-1):
        standing += numbers[i]
        if standing < i+1:
            invite += (i+1)-standing
            standing += (i+1)-standing
    return invite

for i in range(cases):
    ans = solve(filecontents[i][2::])
    print("Case #{}: {}".format(i+1, ans))
