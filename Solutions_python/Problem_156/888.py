import sys
import bisect


def extract_max(pancakes):
    maxval, count = pancakes.pop(-1), 1
    while pancakes and pancakes[-1] == maxval:
        pancakes.pop(-1)
        count += 1
    return maxval, count


def serve(pancakes, penalty=0):
    #  assume pancakes are sorted
    maxval, count = extract_max(pancakes)
    best = maxval + penalty
    #  split maxval to split1, split2
    for split1 in range(1, maxval / 2 + 1):
        split2 = maxval - split1
        assert split2 >= split1
        if split2 + count > maxval: #  check if worth splitting
            continue
        test = pancakes[:]
        for _ in range(count):
            bisect.insort(test, split1)
            bisect.insort(test, split2)
        test_best = serve(test, penalty + count)
        if test_best < best:
            best = test_best
    return best


def main(file_name):
    input_file = open(file_name, "r")
    out_file = open("%s.ans" % file_name, "w")
    cases = int(input_file.readline().strip())
    for i in range(cases):
        D = int(input_file.readline())
        si = sorted(map(int, input_file.readline().split(" ")))
        assert D == len(si), "%d != len(%s)" % (D, si)
        out = serve(si)
        out_file.write("Case #%d: %d\n" % (i + 1, out))
    out_file.close()
    input_file.close()

if __name__ == "__main__":
   main(sys.argv[1])
