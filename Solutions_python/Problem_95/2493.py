import re
import sys

def create_dict():
    res = list(re.sub(r'\s', '', "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv qz"))
    eng = list(re.sub(r'\s', '', "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up zq"))
    dic = {}
    for i in range(0, len(res)):
        dic[res[i]] = eng[i]
    dic[' '] = ' '
    return dic

def to_english(dic, res):
    eng = []
    for i in range(0, len(res)):
        eng.append(dic[res[i]])
    return ''.join(eng)

def get_tc():
    num = int(sys.stdin.readline())
    tc = []
    for i in range(0, num):
        tc.append(sys.stdin.readline().strip())
    return tc

mydic = create_dict()
tc = get_tc()
for i in range(0, len(tc)):
    print "Case #" + str(i+1) + ": " + to_english(mydic, tc[i])
