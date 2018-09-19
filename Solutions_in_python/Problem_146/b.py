# -*- coding: utf-8 -*-
def check_valid_ar(ar):
    border_dic = []
    inner_dic = []
    for s in ar:
        if not check_valid(s, border_dic, inner_dic):
            return False
    return True


def check_valid(s, border_dic, inner_dic):
    l = len(s)
    dic = []
    for i in xrange(l):
        if s[i] in dic:
            if i-1 != 0 and s[i] != s[i - 1]:
                return False
        else:
            dic.append(s[i])
    if len(dic) > 2:
        for i in xrange(1, len(dic) - 1):
            if dic[i] in inner_dic or dic[i] in border_dic:
                return False
            else:
                inner_dic.append(dic[i])

    if dic[0] in inner_dic or dic[len(dic) - 1] in inner_dic:
        return False
    else:
        if dic[0] not in border_dic:
            border_dic.append(dic[0])
        if dic[len(dic) - 1] not in border_dic:
            border_dic.append(len(dic) - 1)
    return True


def get_box(s):
    return (s[0], s[len(s) - 1])


if __name__ == "__main__":
    t = int(raw_input())
    for case_nr in xrange(1, t + 1):
        n = int(raw_input())
        ar = map(str, raw_input().strip().split())
        if not check_valid_ar(ar):
            print "Case #%d: 0" % case_nr
            continue
        train = {}
        flag = True
        for s in ar:
            b = get_box(s)
            if b in train:
                if b[0] == b[1]:
                    train[b] += 1
                else:
                    print "Case #%d: 0" % case_nr
                    flag = False
                    break
            else:
                train[b] = 1
        if not flag:
            continue
        count = 0
        flag = True
        for key in train.keys():
            key_flag = True
            for key2 in train.keys():
                if key != key2:
                    if key2[1] == key[0] and key[1] == key2[0]:
                            print "Case #%d: 0" % case_nr
                            flag = False
                            break
                    if key2[1] == key[1] or key2[0] == key[0]:
                        if key[0] != key[1] and key2[0] != key2[1]:
                            print "Case #%d: 0" % case_nr
                            flag = False
                            break
                    if key2[1] == key[0]:
                        key_flag = False
                        continue

            if not flag:
                break
            if key_flag:
                count += 1
        if not flag:
            continue
        ans = 1
        for i in xrange(1, count + 1):
            ans *= i
            ans = ans % 1000000007
        for key in train.keys():
            t_ans = 1
            if train[key] > 1:
                for j in xrange(1, train[key] + 1):
                    t_ans *= j
            ans *= t_ans
            ans = ans % 1000000007
        print "Case #%d: %d" % (case_nr, ans)
