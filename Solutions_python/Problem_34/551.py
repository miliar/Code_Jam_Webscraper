#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Trie:

    def __init__(self):
        self.trie = 26*[None]

    def add(self, word):
        self.__add(word, self.trie)

    def find(self, pattern):
        return self.__find(pattern, self.trie)

    def __find(self, pattern, trie):
        if pattern == '':
            return 1
        if pattern[0] == '(':
            end = pattern.find(')')
            sum = 0
            for c in pattern[1:end]:
                sum += self.__find(c+pattern[end+1:], trie)
            return sum
        else:
            pos = ord(pattern[0])-ord('a')
            if trie[pos]:
                return self.__find(pattern[1:], trie[pos])
            else:
                return 0

    def __add(self, word, trie):
        if word == '':
            return
        pos = ord(word[0])-ord('a')
        if not trie[pos]:
            trie[pos] = 26*[None]
        self.__add(word[1:], trie[pos])



if __name__ == '__main__':
    line = raw_input().split()
    L = int(line[0])
    D = int(line[1])
    N = int(line[2])
    
    t = Trie()
    for i in range(D):
        t.add(raw_input())

    for i in range(N):
        print 'Case #%d: %d' % (i+1, t.find(raw_input()))



