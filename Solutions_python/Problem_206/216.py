input = open('A-large.in', 'r')
output = open('A-large.out', 'w')
t = int(input.readline().rstrip())
for test in range(t):
    output.write("Case #" + str(test + 1) + ": ")
    d, n = map(int, input.readline().rstrip().split())
    horses = [list(map(int, input.readline().rstrip().split())) for i in range(n)]
    horses.sort(reverse=True)
    maxTime = 0
    for i in range(n):
        maxTime = max(maxTime, (d - horses[i][0]) / horses[i][1])
    print(d / maxTime, file = output)

input.close()
output.close()