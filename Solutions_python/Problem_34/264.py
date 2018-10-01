#!/usr/bin/python

import psyco
psyco.full()

import sys

def build_dict(words):
    d = {}
    for word in words:
        cur_dict = d
        for l in word:
            if l not in cur_dict:
                cur_dict[l] = {}
            cur_dict = cur_dict[l]
        cur_dict['word'] = word
    return d

def word_in_dict(word, dict):
    if len(word) == 0:
        if 'word' in dict:
            return 1
        return 0
    if word[0] != '(':
        if word[0] not in dict:
            return 0
        d = dict[word[0]]
        word = word[1:]
        return word_in_dict(word, d)
    last = word.index(')')
    possible = word[1:last]
    num = 0
    w = word[last+1:]
    for p in possible:
        if p in dict:
            d = dict[p]
            num += word_in_dict(w, d)
    return num

def main():
    L, D, N = map(int, raw_input().split())
    words = set()
    for i in range(D):
        words.add(raw_input().strip())
    sys.stderr.write("building\n")
    d = build_dict(words)
    sys.stderr.write("built\n")
    for i in range(1, N+1):
        word = raw_input().strip()
        n = word_in_dict(word, d)
        print "Case #%d: %d" % (i, n)
        sys.stderr.write(str(i) + "\n")

if __name__ == "__main__":
    main()
