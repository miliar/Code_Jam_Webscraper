#!/usr/bin/python

import re


input_file = open('A-large.in')
output_file = open('output', 'w')

(L, D, N) = map(int, input_file.readline().split(' '))

words = list()
for d in range(D):
    words.append(input_file.readline().rstrip("\n"))


for n in range(N):
    msg = input_file.readline().rstrip("\n")
    K = 0

    msg_array = [tmp.replace('(', '').replace(')', '') for tmp in re.findall('\([a-z]*\)|[a-z]', msg)]
    for word in words:
        i = 0
        for c in word:
            if not (c in msg_array[i]):
                break
            i += 1
        else:
            K += 1

    output_file.write("Case #" + str(n + 1) + ": " + str(K) + "\n")

input_file.close()
output_file.close()
