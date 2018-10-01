__author__ = 'danolsen'

with open('input/b-large.txt') as fin:
    cases = int(fin.readline())

    with open('output/b-large.txt', 'w') as out:
        for i in range(1, cases + 1):
            vals = fin.readline().split()

            c = float(vals[0])
            f = float(vals[1])
            x = float(vals[2])

            cookies_per_second = 2
            curr_min = float(x / cookies_per_second)
            iter = 0
            min_hit = False
            start = int(x/c-10)
            end = int(x/c+10)

            for j in range(start, end):
                if min_hit:
                    break
                total = 0
                farms = 0
                cookies_per_second = 2

                for k in range(0, j):
                    time_for_farm = float(c / cookies_per_second)

                    total += time_for_farm
                    cookies_per_second = 2 + ((k+1) * f)
                total += float(x / cookies_per_second)
                if (curr_min is None or total < curr_min) and total != 0:
                    curr_min = total
                    iter = j

            out.write('Case #%d: %.7f\n' % (i, curr_min))

