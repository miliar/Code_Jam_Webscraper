
def is_tidy(n):
    """Return if n's digits are all in non asending order"""
    last = 0
    for ii in str(n):
        if ii < last:
            return False
        last = ii
    return True

def make_tidy(n):
    """ Converts int-able string n to a tidy int-able string"""
    # Forward, find the start of 9s
    flat = list(str(n))
    edgeFound = False
    for idx in xrange(len(flat)):
        if idx is 0:
            continue
        # fillng in 9s
        elif edgeFound:
            flat[idx] = '9'
            continue
        elif int(flat[idx-1]) > int(flat[idx]):
            edgeFound = True
            flat[idx] = '9'
            flat[idx-1] = str(int(flat[idx-1])-1)
    # Backward,
    flat = list(reversed(flat))
    for idx in xrange(len(flat)):
        if idx is len(flat)-1:
            continue
        elif flat[idx] < flat[idx+1]:
            flat[idx:idx+2] = ['9',str(int(flat[idx+1]) -1)]
    #int wipes out 0 pag
    return int(''.join(reversed(flat)))

def process_input():
    # Skip number of test cases
    t = int(raw_input())  # read a line with a single integer
    for ii in xrange(1, t + 1):
        numb = raw_input()
        if numb < 10 or is_tidy(numb):
            n = numb
        else:
            n = make_tidy(numb)
        print('Case #{ii}: {n}'.format(ii=ii, n=n))


def test():
    def istidytest():
        assert is_tidy(129)
        assert is_tidy(999)
        assert is_tidy(7)
        assert is_tidy(99999999999999999)
        assert is_tidy(8)
        assert is_tidy(123)
        assert is_tidy(555)
        assert is_tidy(224488)
    def isnottidytest():
        assert not is_tidy(132)
        assert not is_tidy(1000)
        assert not is_tidy(111111111111111110)
        assert not is_tidy(20)
        assert not is_tidy(231)
        assert not is_tidy(495)
        assert not is_tidy(999990)
    def maketidyexacttest():
        assert is_tidy(make_tidy(132))
        assert is_tidy(make_tidy(1000))
        assert is_tidy(make_tidy(7))
        assert is_tidy(make_tidy(111111111111111110))
    def maketidyrandomtest():
        for ii in xrange(10**3):
            assert is_tidy(make_tidy(ii)), 'Failed to make {} tidy'.format(ii)

    istidytest()
    isnottidytest()
    maketidyexacttest()
    maketidyrandomtest()


if __name__ == '__main__':
    #test()
    process_input()