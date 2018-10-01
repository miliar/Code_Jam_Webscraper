def is_tidy(s):
    for digitIdx in range(s) - 1:
        if s[digitIdx] >= s[digitIdx+1]:
            return False
    return True

def borrow(inputStr, idx):
    print(''.join(reversed(inputStr)) + ' ' + str(idx))
    for i in range(idx+1, len(inputStr)):
        print(i)
        if inputStr[i] != '0':
            inputStr[i] = str(int(inputStr[i])-1)
            inputStr[:i] = '9' * len(inputStr[:i])
            print('len = ' + str(len(inputStr[:i])))
            break
    print('ans ' + ''.join(reversed(inputStr)))
"""
borrow(list('789'),0)
borrow(list('979'),1)
borrow(list('789'),1)
exit()
"""
fh = open('prob2.txt','w')
test_num = int(input())
for caseIter in range(test_num):
    inputRevStr = list(str(int(input())))
    inputRevStr.reverse()
    if len(inputRevStr) == 1:
        fh.write('Case #' + str(caseIter+1) + ': ' + ''.join(inputRevStr) + '\n')
    else:
        for idx in range(len(inputRevStr) - 1):
            if inputRevStr[idx] >= inputRevStr[idx+1]:
                continue
            else:
                borrow(inputRevStr, idx)
        inputRevStr.reverse()
        fh.write('Case #' + str(caseIter+1) + ': ' + str(int(''.join(inputRevStr))) + '\n')
fh.close()
