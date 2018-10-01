def lst_tidy(num):
    while num>0:
        if is_tidy(num):
            return num
        else:
            num = make_tidy(num)



def is_tidy(num):
    num = list(str(num))
    prev_dig = 9
    for dig in num:
        if dig >= prev_dig:
            prev_dig=dig
        else:
            return False
    return True

def make_tidy(num):
    num=str(num)
    prev_dig = int(num[0])
    for i in xrange(len(num)): #find untidiness
        if int(num[i]) >= prev_dig: prev_dig=int(num[i])
        else: #make tidy
            newnum = num[:i]
            for d in range(len(num)-i): newnum += "0"
            return int(newnum)-1




def main():

    n = int(raw_input())
    for case in range(1, n+1):
        num = int(raw_input())
        print "Case #{}: {}".format(case,lst_tidy(num))


main()