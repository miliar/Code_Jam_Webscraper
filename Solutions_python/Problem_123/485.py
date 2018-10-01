import argparse


def read_input(input_file):
    number_of_test_cases = input_file.readline()
    for case in xrange(1, int(number_of_test_cases) + 1):
        mote_info = [int(i) for i in input_file.readline().strip('\n').split(' ')]
        armin_mote_size = mote_info[0]
        motes_qty = mote_info[1]
        motes = [int(m) for m in input_file.readline().strip('\n').split(' ')]
        answer = compute_answer(armin_mote_size, motes_qty, motes)
        print 'Case #%d: %s' % (case, answer)


def compute_answer(*args):
    armin_mote = args[0]
    motes_qty = args[1]
    motes = args[2]

    if armin_mote == 1:
        return motes_qty

    motes.sort()
    count = 0
    for m in motes:
        if armin_mote > m:
            armin_mote += m
        elif motes.index(m) < motes_qty - 1 and m > 1:
            while armin_mote <= m:
                armin_mote += armin_mote - 1
                count += 1
            armin_mote += m
        else:
            count += 1
    if count <= motes_qty:
        return count
    else:
        return motes_qty


def main(input_file):
    read_input(input_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=file)
    args = parser.parse_args()
    main(args.input_file)
