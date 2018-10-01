
def numOfFriend(s, aud):
    out = 0
    stand = aud[0]
    i = 1
    while i <= s and stand < s:
        if i > stand:
            out += 1
            stand += 1
        stand += aud[i]
        i += 1
    return out

if __name__=="__main__":
    numOfCase = input()
    for c in range(0,numOfCase):
        case_str = raw_input().split()
        s_max = int(case_str[0])
        aud = []
        for i in range(0,s_max+1):
            aud.append(int(case_str[1][i]))

        output = numOfFriend(s_max, aud)
        print("Case #%d: %d" % (c+1,output))
