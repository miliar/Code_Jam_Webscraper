def is_tidy(n):
    n_str = str(n)
    for i in range(len(n_str) - 1):
        if int(n_str[i]) > int(n_str[i+1]):
            return False
    return True

def find_min_tidy(n):
    if is_tidy(n):
        return n
    else:
        return find_min_tidy(n-1)

def main():
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n = raw_input()

        min_tidy = find_min_tidy(int(n))

        print "Case #{}: {}".format(i, min_tidy)

if __name__ == '__main__':
    main()
