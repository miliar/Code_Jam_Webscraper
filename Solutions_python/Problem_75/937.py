#! /usr/bin/python
from sys import argv

def open_file(file_name):
    res = []
    fin = open(file_name)
    lines = fin.readlines()
    fin.close()
    test_cases = lines[0] # who needs this crap
    del lines[0]
    # CN 3C0 ... 3CN DN 2D0 .... 2DN n 0 ... n
    # C's are combined words
    # D's are opp words
    # N are the list to be invoked
    for line in lines:
        line = line.strip()
        #print "line is ", line
        combo_dict = {}
        opp_dict = {}
        prb_list = []
        kase = line.split()
        # get no. of combowords
        no_of_combo = int(kase[0])
        del kase[0]
        combo_dict = get_combo_dict(no_of_combo, kase)
        #print "combo is ", combo_dict
        kase = clear_list(kase, no_of_combo)
        no_of_opp = int(kase[0])
        del kase[0]
        opp_dict = get_opp_dict(kase,no_of_opp)
        kase = clear_list(kase, no_of_opp)
        prb_list = kase[1]
        #print "opp is ", opp_dict
        #print "prb is ", prb_list
        res.append(get_magica_list(prb_list, combo_dict, opp_dict))
    return res
        
def get_magica_list(prb_list, combo_dict, opp_dict):
    ret = ""
    for ele in prb_list:
        ret += ele
        if len(ret) <= 1:
            continue
        ret = magica(ret, combo_dict, opp_dict)
        orig = ret
        while(True):
            if len(ret) > 1:
                ret = magica(ret, combo_dict, opp_dict)
            if ret == orig:
                break
            else:
                orig = ret
    return "[%s]" % ", ".join(list(ret))


def magica(ret, combo_dict, opp_dict):
        #print "in magica", ret
        ele = ret[-1]
        wrd = ret[-2:]
        if wrd in combo_dict:
            #print "word is ", wrd
            ret = ret[:-2] + combo_dict[wrd]
        elif ele in opp_dict:
            if opp_dict[ele] in ret:
                ret = ""
        return ret

def get_combo_dict(limit, line):
    cmd_dict = {}
    for i in range(limit):
        wrd = line[i]
        key = wrd[:2]
        val = wrd[-1]
        cmd_dict[key] = val
        cmd_dict[key[::-1]] = val
    return cmd_dict

def get_opp_dict(t, limit):
    opp_dic = {}
    for i in range(limit):
        wrd = t[i]
        key = wrd[0]
        val = wrd[-1]
        opp_dic[key] = val
        opp_dic[val] = key
    return opp_dic

def clear_list(list, limit):
    for i in range(limit):
        list.pop(0)
    return list


def write_out(res):
    fin = open('pout.txt','w')
    count = 0
    for item in res:
        count += 1
        fin.write("Case #%d: %s" %(count,item))
        fin.write("\n")
    fin.close()

script, file_name = argv
res = open_file(file_name)
write_out(res)
