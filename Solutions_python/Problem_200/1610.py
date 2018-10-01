def cal(number):
    x = list(number)
    p = len(x)-1

    while p > 0:
        # compare
        if x[p] < (x[p - 1]):
        # change the value of pointer to 9
            c = p
            while c < len(x):
                x[c] = str(9)
                c+= 1
            y = int(x[p-1]) - 1
            x[p - 1] = str(y)
            p = p - 1
        else:
            p = p - 1
            # move the pointer
    if(x[0] == "0"):
        x.pop(0)
    return ''.join(x)




def main():
    f = open('B-large.in', 'r')
    w = open('out.txt', 'w')
    i = 0
    for line in f:
        if i:
            ans = cal(line.strip())
            res = "Case #"+str(i)+": "+ans
            w.write(res+'\n')
        i+=1
    f.close()
    w.close()
main()