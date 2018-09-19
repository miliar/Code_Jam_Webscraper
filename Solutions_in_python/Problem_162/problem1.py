__author__ = 'lyc'

def reverse(num):
  return int(str(num)[::-1])

def dp(num):
    res = []
    res.append(0)
    for i in range(1, num + 1):
        if i <= 20:
            res.append(i)
        else:
            if reverse(i) < i and i % 10 != 0:
                res.append(min(res[reverse(i)] + 1, res[-1] + 1))
            else:
                res.append(res[-1] + 1)
    return res[-1]




def CounterCulture(num, cur, res):
    if num <= 20:
        return num
    elif cur == num - 1:
        return res + 1
    elif cur == num:
        return res
    elif cur > num:
        return
    print num, cur, res
    if reverse(cur) > cur and reverse(cur) < num:
        return min(CounterCulture(num, reverse(cur), res + 1), CounterCulture(num, cur + 1, res + 1))
    else:
        return CounterCulture(num, cur + 1, res + 1)



def main():
    f = open("A-small-attempt1.in")
    wr = open("res1.txt", "w")
    i = 0
    for line in f:
        if i == 0:
            i += 1
            continue
        else:
            print line
            print str(dp(int(line)))
            wr.write("Case #" + str(i) + ": " + str(dp(int(line))) + "\n")
        i = i + 1

main()