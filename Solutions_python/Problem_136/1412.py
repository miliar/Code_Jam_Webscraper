import sys

fh = open(sys.argv[1])
oh = open("output.txt", "w")

t = int(fh.readline().strip())
test_no = 1

for line in fh.readlines():
    if not line:
        continue

    (c, f, x) = [float(i) for i in line.split(' ')]
    t = 0.0
    r = 2.0
    cookies = 0.0

    while cookies < x:
        time_to_buy_farm = (c-cookies)/r
        time_to_buy_farm_and_finish = time_to_buy_farm + (x)/(r+f)
        time_to_finish = (x-cookies)/r

        if time_to_buy_farm_and_finish < time_to_finish:
            cookies = 0
            r = r + f
            t = t + time_to_buy_farm
        else:
            break

    t = t+time_to_finish

    ans = "Case #%d: %s\n" % (test_no, str(round(t, 7)))
    oh.write(ans)
    test_no += 1

oh.close()
fh.close()
