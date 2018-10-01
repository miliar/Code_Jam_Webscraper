test_cases = int(input())
case = 1

for test in range(test_cases):
    print("Case #",end="")
    print(case, end="")
    print(": ", end="")
    [c, f, x] = map(float, input().split())
    t = 0
    speed = 2.0
    if x <= c:
        print(x/speed)
        case = case + 1
        continue
    t = c/speed
    while(x/(f+speed) < (x-c)/speed):
        speed  = speed + f
        t = t+ c/speed
    t = t + (x-c)/speed
    case = case + 1
    print(t)
