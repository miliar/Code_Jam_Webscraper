import xml.etree.ElementTree as etree
import numpy as np
import pickle
import re
from os import listdir
from os.path import isfile, join, abspath, basename
from collections import Counter, defaultdict
from sklearn import svm
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.decomposition import PCA


def read_lines_from_file(filename):
    with open(filename, mode='r+', encoding='utf-8') as fp:
        lines = fp.readlines()
    lines = [l.rstrip() for l in lines]
    return lines

def write_lines_to_file(lines, filename):
    with open(filename, mode='wt', encoding='utf-8') as fp:
        fp.write('\n'.join(x for x in lines))


def get_largest_tidy(strval):
    index = 0
    direction = True # right:1, left:0
    chars = list(strval)
#     print(chars)
    # Move from left to right
    while (index < len(chars) - 1 and direction):
        if chars[index] <= chars[index + 1]:
            index += 1
            continue
        chars[index] = str(int(chars[index]) - 1)
        for i in range(index + 1, len(chars)):
            chars[i] = '9'
#         print(chars)
#         if chars[index] != '0':
#             break        
        direction = False
        break
        
    # Move from right to left
    while (index > 0 and not direction):
#         print(index, chars[index], chars[index - 1])
        if chars[index] >= chars[index - 1]:
            break
#         if chars[index] == '0':
        chars[index] = '9'
        index -= 1
        chars[index] = str(int(chars[index]) - 1)
        
    res = int(''.join(chars))
    return res


testfile = 'B-large.in' # 'sampleB.txt'
cases = read_lines_from_file(testfile)[1:]
res = [0] * len(cases)
print(cases)


results = []
for i in range(len(cases)):
    tidy = get_largest_tidy(cases[i])
    results.append("Case #" + str(i + 1) + ': ' + str(tidy))
    write_lines_to_file(results, 'B-large.out') # 'resultB.txt'