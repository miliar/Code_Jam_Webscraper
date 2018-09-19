import os
import sys

sys.setrecursionlimit(10**9)
input_path = 'in.txt'
output_path = 'out.txt'


def read_line():
    line = ''
    while len(line) == 0:
        line = input_file.readline().strip()
    return line


def write_line(line):
    return output_file.write(line+'\n')


mc = None
sentences = []

def search(x, eng, fre):
    count = len(eng & fre)
    if x == -1:
        global mc
        if mc is None or count < mc:
            mc = count
        return count
    if mc is not None and count > mc:
        return count
    return min(search(x - 1, sentences[x] | eng, fre), search(x - 1, eng, sentences[x] | fre))


def solve():
    n = int(read_line())
    global sentences
    global mc
    mc = None
    sentences = [set(read_line().split(' ')) for i in xrange(n)]
    eng = sentences[0]
    fre = sentences[1]
    sentences = sentences[2:]
    return search(len(sentences) - 1, eng, fre)


input_file = open(input_path, "r")
output_file = open(output_path, "w+")
T = int(read_line())
for case_id in xrange(1, T + 1):
    write_line("Case #%d: %s" % (case_id, solve()))
input_file.close()
output_file.close()