# code jam qualification round
# Problem A. Speaking in Tongues

def get_char_mapping(encrypted, decrypted, dic):
    pos=0
    
    for e in encrypted:
        d = decrypted[pos]
        dic[e] = d
        pos += 1

    return dic

def decrypt (encrypted, d):
    res=""
    for c in encrypted:
        if '\n' == c:
            continue
        res += d[c]

    return res

input1  = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
output1 = "our language is impossible to understand"

input2  = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
output2 = "there are twenty six factorial possibilities"

input3  = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
output3 = "so it is okay if you want to just give up"

d = {}
get_char_mapping(input1, output1, d)
get_char_mapping(input2, output2, d)
get_char_mapping(input3, output3, d)
d['y'] = 'a'
d['a'] = 'y'

d['e'] = 'o'

d['q'] = 'z'
d['z'] = 'q'

import sys

def main():
    print decrypt("y qee", d)
    
    f = open('A-small-attempt1.in', 'r')
    r = open('A-small-attempt1.in-result', 'w')
 
    while True:
        line = f.readline()
        if not line:
            break
        caseNum = int(line)
        for i in range(caseNum):
            line = f.readline()
            result_line = "Case #"+str(i+1)+": " + decrypt(line, d)
            r.write(result_line + '\n')
            # print result_line
 
    f.close()
    r.close()

if __name__ == '__main__':
    main()

