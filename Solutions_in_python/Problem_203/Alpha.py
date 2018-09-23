def split(str):
    return list ( str )

def checkEqual_list(lst):
   return lst[1:] == lst[:-1]

test_cases = int(raw_input())
for i in range (0, test_cases):
    inputs = raw_input().split()
    r = int(inputs[0])
    c = int(inputs[1])
    out_put = []
    old_out_str = ''
    count = 0
    for k in range(0, r):
        temp = []
        out = []
        strr = split(raw_input())
        out_str = ''
        for j in range(0, c):
            if checkEqual_list(strr):
                if '?' in strr:
                    if j == 0:
                        if old_out_str == '':
                            count = count + 1
                        else:
                            out_put.append(old_out_str)
                else:
                    if j == 0:
                        out_put.append(''.join(strr))
                        old_out_str = ''.join(strr)
            else:
                if j>0 and strr[j] != strr[j-1]:
                    new_temp = []
                    if strr[j-1] == '?':
                        for x in temp:
                            new_temp.append(strr[j])
                        out.append(new_temp)
                        temp = [strr[j]]
                    elif strr[j] == '?':
                        strr[j] = strr[j-1]
                        temp.append(strr[j-1])
                    else:
                        out.append(temp)
                        temp = [strr[j]]
                else:
                    temp.append(strr[j])
                out_str = ''.join(''.join(e) for e in out)+ ''.join(str(e) for e in temp)
        if len(out_str)>0:
            old_out_str = out_str
            out_put.append(out_str)
    print("Case #" + str(i+1) + ":")
    for items in out_put:
        if count > 0:
            for c in xrange(0, count):
                print(items)
            count = 0
        print(items)



