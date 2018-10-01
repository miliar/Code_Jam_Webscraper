input = open('B-small-attempt0.in', 'r')
output = open('B-small-attempt0.out', 'w')
t = int(input.readline().rstrip())
for test in range(t):
    output.write("Case #" + str(test + 1) + ": ")
    ac, aj = map(int, input.readline().rstrip().split())
    cam = sorted([list(map(int, input.readline().rstrip().split())) for i in range(ac)])
    jam = sorted([list(map(int, input.readline().rstrip().split())) for i in range(aj)])
    if ac == 2:
        if cam[1][0] - cam[0][1] >= 720 or cam[1][1] - cam[0][0] <= 720:
            print(2, file = output)
        else:
            print(4, file = output)
    elif aj == 2:
        if jam[1][0] - jam[0][1] >= 720 or jam[1][1] - jam[0][0] <= 720:
            print(2, file = output)
        else:
            print(4, file = output)
    else:
        print(2, file = output)
    
input.close()
output.close()