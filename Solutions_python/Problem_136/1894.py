import sys

def test(file):
    c, f, x = [ float(v) for v in file.readline().split() ]
    cps = 2
    total_time = 0.0
    while True:
        time_to_win = x/cps
        time_to_buy_farm = c/cps
        time_to_win_with_farm = x/(cps+f) + time_to_buy_farm
        if time_to_win < time_to_win_with_farm:
            # stop
            return total_time + time_to_win
        else:
            cps += f
            total_time += time_to_buy_farm


def main(argv):
    if len(argv) < 2:
        return
    filename = argv[1]
    with open(filename) as f:
        num_tests = int(f.readline())
        for i in range(num_tests):
            res = test(f)
            print( "Case #", i+1, ": ", format(res, "#.7f"), sep='')

if __name__ == "__main__":
    main(sys.argv)