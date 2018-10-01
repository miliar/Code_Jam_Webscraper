__author__ = 'nguyensontung1404'

def eliminate(_str):
    if "\n" in _str:
        return _str[:-1]
    else:
        return _str

def take_no_action(_list):
    origin = _list[0]
    for s in _list:
        if s != origin:
            return False
    return True

def simplify(s):
    re = s[0]
    pre = s[0]
    for c in s[1:]:
        if c != pre:
            re += c
            pre = c
    return re

def make(_string):
    re = []
    ori = _string[0]
    count = 0
    for i in range(len(_string)):
        if _string[i] == ori:
            count += 1
        if _string[i] != ori:
            re.append([_string[i-1], count])
            ori = _string[i]
            count = 1
        if i == len(_string) - 1:
            re.append([_string[i], count])
    return re

def impossible(l):
    ori = simplify(l[0])
    for _str in l:
        if simplify(_str) != ori:
            return True
    return False

def make(_string):
    re = []
    ori = _string[0]
    count = 0
    for i in range(len(_string)):
        if _string[i] == ori:
            count += 1
        if _string[i] != ori:
            re.append([_string[i-1], count])
            ori = _string[i]
            count = 1
        if i == len(_string) - 1:
            re.append([_string[i], count])
    return re


def cal(x, y):
    l1 = make(x)
    l2 = make(y)
    count = 0
    for i in range(len(l1)):
        count += abs(l1[i][1] - l2[i][1])
    return count

if __name__ == "__main__":
    import sys
    sys.stdin = open("A-small-attempt0.in")
    sys.stdout = open("out.txt", "w")
    for case in range(1, int(sys.stdin.readline())+1):
        N = int(sys.stdin.readline())
        _list = []
        for i in range(N):
            _list.append(eliminate(sys.stdin.readline()))
        if take_no_action(_list):
            print "Case #%d: 0" % case
        else:
            if impossible(_list):
                print "Case #%d: Fegla Won" % case
            else:
                print "Case #%d: %d" % (case, cal(_list[0], _list[1]))
