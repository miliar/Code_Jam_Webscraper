def is_tidy(n):
    n_ = str(n)
    return sorted(n_) == list(n_)

def last_tidy(n):
    for s in range(n, 0, -1):
        if is_tidy(s): return s

def last_tidy_(n):
    n_ = list(str(n))
    for i in range(0, len(n_)-1):
        if n_[i] > n_[i+1]:  # yuck!
            n_[i] = str(int(n_[i]) - 1)
            for j in range(i+1, len(n_)):
                n_[j] = '9'
            n = int(''.join(n_))
            return last_tidy_(n)
    assert is_tidy(n), n
    return n

if __name__ == '__main__':
    import io
    for i, line in enumerate(io.open('B-large.in', 'r').readlines()):
        if i == 0: continue
        n = int(line)
        #assert last_tidy(n) == last_tidy_(n)
        print('Case #{}: {}'.format(i, last_tidy_(n)))