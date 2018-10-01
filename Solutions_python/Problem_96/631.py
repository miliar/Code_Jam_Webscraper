#Dancing


t = int(raw_input())
for i in range(0,t):
    input = raw_input().split(" ")
    n = int(input[0])
    s = int(input[1])
    p = int(input[2])
    count = 0
    for j in range(3,3+n):
        leftover = int(input[j]) - p

        if leftover < 0:
            1
        elif leftover >= (2*p - 2):
            count += 1
        else:
            if s > 0:
                if leftover >= (2*p - 4):
                    s -= 1
                    count += 1
    print "Case #" + str(i+1) + ": " + str(count)
