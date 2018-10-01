input = open("input.txt", "r")

cases = int(input.readline())

with open('large_results.txt', 'w') as results:
    for case in range(cases):
        s_max, audience = input.readline().split()
        num_friends = 0
        total_audience = 0
        for s_idx, s in enumerate(audience):
            if total_audience >= s_idx:
                total_audience += int(s)
            else:
                while total_audience < s_idx:
                    num_friends += 1
                    total_audience += 1
                total_audience += int(s)
        to_write = "Case #%i: %s" % (case+1, num_friends)
        print to_write
        results.write(to_write + "\n")

input.close()