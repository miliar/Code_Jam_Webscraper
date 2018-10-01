def main():
    t = int(input())
    cases = []
    for i in range(0, t):
        line = input()
        nums = line.split()
        d = int(nums[0])
        n = int(nums[1])
        horses = []
        for j in range(0, n):
            line = input()
            nums = line.split()
            k = int(nums[0])
            s = int(nums[1])
            horses.append((k, s))

        cases.append((d, horses))

    #print(cases)

    for i in range(0, t):
        case = cases[i]
        min_time = 0
        d = case[0]
        horses = case[1]
        for horse in horses:
            k = horse[0]
            s = horse[1]
            time = (d - k) / s
            if time > min_time:
                min_time = time

        speed = d / min_time

        print("Case #{0}: {1}".format(i+1, speed))

main()
