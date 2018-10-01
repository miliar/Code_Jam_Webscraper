def describe_num(n_str):
    grow_pos = 0
    breaking_pos = None
    prev = None
    for i, d in enumerate(n_str):
        if prev < d:
            prev = d
            grow_pos = i
        elif prev > d:
            breaking_pos = i
            break
    return grow_pos, breaking_pos


def prev_tidy(n_str):
    grow_pos, breaking_pos = describe_num(n_str)
    if breaking_pos is None:
        return n_str
    n_lst = list(n_str)
    n_lst[grow_pos] = str(int(n_lst[grow_pos]) - 1)
    for i in range(grow_pos+1, len(n_str)):
        n_lst[i] = '9'
    return ''.join(n_lst).lstrip('0')


def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
      res = prev_tidy(raw_input())
      print "Case #{}: {}".format(i, res)


if __name__ == "__main__":
    main()
