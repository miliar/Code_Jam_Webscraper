## QUESTION 2


def calc_correct_lst(c_lst, d_lst, string, c, d, s_len, c_lst2 = [], dangers = ''):

    if c_lst2 == []:
        c_lst2 = [x[:2] for x in c_lst]
        c_lst2.extend([x[::-1] for x in c_lst2])

    rules_lst2 = [False] * s_len

    if dangers == '' and d > 0:
        d_lst.extend([x[::-1] for x in d_lst])
        dangers = ''.join(d_lst)

    result_lst = []
    
    for i in range(1, s_len):
        if string[i-1:i+1] in c_lst2 and (not rules_lst2[i - 1]):
            rules_lst2[i] = True

    for i in range(1, s_len):
        if (string[i] in dangers) and (not rules_lst2[i]):
            for x in d_lst:
                if x[0] == string[i]:
                    for j in range(i):
                        if string[j] == x[1] and (not (rules_lst2[j] or rules_lst2[j + 1])):
                            return calc_correct_lst(c_lst, d_lst, string[i + 1:], c, d, s_len - (i + 1), c_lst2, dangers)
                        
    for i in range(s_len):
        if rules_lst2[i]:
            m = string[i-1:i+1]
            ind = c_lst2.index(m)
            result_lst[-1] = c_lst[ind % c][2]
        else:
            result_lst.append(string[i])

    return result_lst

def special_to_str(result_lst):
    res = '['
    for x in result_lst[:-1]:
        res += x
        res += ', '
    if len(result_lst) > 0:
        res += result_lst[-1]

    res += ']'
    return res

def solve(filename, out_file):
    lines = [x[:-1] for x in open(filename).readlines()]
    out = open(out_file, 'a')
    times = int(lines[0])
    for i in range(1, times + 1):
        line = lines[i].split(' ')
        c = int(line[0])
        c_lst = line[1:1+c]
        d = int(line[1 + c])
        d_lst = line[2+c:2+c+d]
        s_len = int(line[2+c+d])
        string = line[3+c+d]
        out.writelines('Case #%d: %s\n' % (i, special_to_str(calc_correct_lst(c_lst, d_lst, string, c,d,s_len))))
        
        
