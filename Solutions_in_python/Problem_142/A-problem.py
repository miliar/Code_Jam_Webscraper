#!/usr/bin/python2.7


from decimal import Decimal
from collections import Counter


class FileIO(object):
    """
    Utility to interact with input/output files.
    """

    def __init__(self, input_filename='input.txt', output_filename='output.txt'):
        """
        set the input and output file names.
        """
        self._input = input_filename
        self._output = output_filename
        self._fin = open(self._input, 'r')
        self._fout = open(self._output, 'w')

    def get_row(self):
        """
        get a line row.
        """
        return self._fin.readline().strip('\n').strip(' ')

    def get_int(self):
        return int(self.get_row())

    def get_str_arrays(self):
        """
        get a string array from a line row read from file.
        """
        return self._fin.readline().strip('\n').strip(' ').split(' ')

    def get_int_arrays(self):
        return map(lambda x: int(x), self.get_str_arrays())

    def get_float_arrays(self):
        return map(lambda x: float(x), self.get_str_arrays())

    def get_decimal_arrays(self):
        return map(lambda x: Decimal(x), self.get_str_arrays())

    def write(self, stuffs):
        self._fout.write(stuffs)

    def close(self):
        """
         close used resources.
        """
        self._fin.close()
        self._fout.close()



FEGLA_WON = 'Fegla won'


def find_result(n, words):
    sequences = list()
    for word in words:
        prev_c = None
        seq = list()
        for c in word:
            if c != prev_c:
                if prev_c is not None:
                    seq.append((prev_c, count,))
                count = 1
                prev_c = c
            else:
                count += 1
        if prev_c is not None:
            seq.append((prev_c, count,))
        sequences.append(seq)

    # check possibility of winning
    ref_seq = sequences[0]
    seq_len = len(ref_seq)
    n_sequences = len(sequences)
    for i in range(n_sequences - 1):
        x = i + 1
        curr_seq = sequences[x]
        if len(curr_seq) != seq_len:
            # not the same length, can't win
            return FEGLA_WON
        # ok this is of the same length, lets
        # perform checks
        for j in range(seq_len):
            if ref_seq[j][0] != curr_seq[j][0]:
                return FEGLA_WON
    # ok, now we know we can win, only how many steps?

    n_steps = 0
    for i in range(seq_len):
        sum = 0.0
        for j in range(n_sequences):
            sum += sequences[j][i][1]
        chosen_avg = int(sum/n_sequences + 0.5)
        for j in range(n_sequences):
            n_steps += abs(chosen_avg - sequences[j][i][1])
    return '%d' % n_steps


if __name__ == '__main__':
    # fio = FileIO('../inputs/A-sample.in')
    fio = FileIO('../inputs/A-small-attempt0.in')
    # fio = FileIO('../inputs/A-large-practice.in')
    n_cases = fio.get_int()
    for n in range(n_cases):
        n_words = fio.get_int()
        words = list()
        for i in range(n_words):
            words.append(fio.get_row())
        result = find_result(n_words, words)
        print('Case #%d: %s' % (n + 1, result,))
        fio.write('Case #%d: %s\n' % (n + 1, result,))
    fio.close()

