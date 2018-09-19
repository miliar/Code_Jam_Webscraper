#!/usr/bin/python

from common import *

def consistent(l, word, test_word):
    word_index = 0
    for i in xrange(l):
        if word[word_index] == '(':
            while word[word_index] != ')':
                if word[word_index] == test_word[i]:
                    break
                word_index += 1
            else:
                return False

            while word[word_index] != ')':
                word_index += 1
            word_index += 1

        else:
            if word[word_index] != test_word[i]:
                return False
            word_index += 1
    return True

def main(in_file, out_file):
    l, d, n = readintegers()

    dictionary = []
    for i in xrange(d):
        dictionary.append(readline())

    for x in xrange(n):
        word = readline()
        num_matching = 0
        for test_word in dictionary:
            if consistent(l, word, test_word):
                num_matching += 1

        writeline("Case #%d: %d" % (x + 1, num_matching))

run_main(sys.argv, main)
