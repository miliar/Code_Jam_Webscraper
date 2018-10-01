import math
def isPalindrome(n):
    n = list(str(n))
    start = 0
    back = len(n) - 1
    while start < back:
        if(n[start] == n[back]):
            start += 1
            back -= 1
        else:
            return False
    return True
lines = open('C-small-attempt0.in').read().splitlines()
test_cases = int(lines[0])
groups_one = lines[1:]
groups = []
for line in groups_one:
    groups.append(line.split())
groups = filter(None, groups)
current_case = 1

for line in groups:
    count = 0
    list_of_squares = [x*x for x in range(int(math.ceil((int(line[0])**0.5))), int((int(line[1])**0.5))+1)]
    for square in list_of_squares:
        if(isPalindrome(square)):
            if(isPalindrome(str(int(int(square)**0.5)))):
                count+=1
    print("Case #" + str(current_case) + ": " + str(count))
    current_case +=1
