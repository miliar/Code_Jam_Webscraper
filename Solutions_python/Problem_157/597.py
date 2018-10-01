quaternion = {'1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'}, 'i': {'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j'}, 'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'}, 'k': {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1'}, }


def mult(ai, aj, s):
    ret = quaternion[ai][aj]
    if ret[0] == '-':
        if s == 1: s = 0
        else: s = 1
        ret = ret[1]

    return (ret, s)

if __name__ == '__main__':

    for case in range(1, input()+1):
        xValue = int(raw_input().split()[1]);
        s = raw_input() * xValue
    
        iLookUp, sign, curVal = [], 1, '1'
        for i in range(len(s)-2):
            curVal, sign = mult(curVal, s[i], sign)
            if curVal == 'i' and sign == 1:
                iLookUp.append(i)
    
        kLookUp, sign, curVal = set(), 1, '1'
        if iLookUp:
            for i in range(len(s)-1, 1, -1):
                curVal, sign = mult(s[i], curVal, sign)
                if curVal == 'k' and sign == 1:
                    kLookUp.add(i)

        valid = False
        for i in iLookUp:
            sign, curVal = 1, '1'
            for j in range(i+1, len(s)-1):
                curVal, sign = mult(curVal, s[j], sign)
                if curVal == 'j' and sign == 1:
                    if (j+1) in kLookUp:
                        valid = True
                if valid: 
                    break
            if valid: 
                break

        print 'Case #' + str(case) + ': ' + ('YES' if valid else 'NO')