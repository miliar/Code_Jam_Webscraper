
import sys
import string
import re

def main():
    file = open(sys.argv[1])
    output = open('result.alien', 'w')
    words = []

    # load the numbers and verify the ranges
    l, d, n = [int(x) for x in file.readline().split()]
    if not(1 <= l <= 15): return
    if not(1 <= d <= 5000): return
    if not(1 <= n <= 500): return

    # load the words
    for i in range(d):
        word = file.readline()[:-1]
        if len(word) == l:
            words.append(word)

    template = "Case #%d: %d\n"
    for i in range(n):
        pattern = convert_to_pattern(file.readline()[:-1])
        count = count_words(words, pattern)
        output.write(template%((i+1, count)))

def convert_to_pattern(word):
    word = re.sub(r'\(', '[', word)
    word = re.sub(r'\)', ']', word)
    return word

def count_words(words, pattern):
    p = re.compile(pattern)
    count = 0
    for word in words:
        if p.match(word):
            count += 1
    return count
main()
