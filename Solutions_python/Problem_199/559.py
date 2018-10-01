def ret_minus(seq, num, k):
    return [ -1*seq[num+i] for i in xrange(k)]

if __name__ == "__main__":
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        pancakes = raw_input().split(" ");
        seq = pancakes[0];
        size = int(pancakes[1]);
        flag = 0


        seql = []
        for j in seq:
            if(j == "+"):
                seql.append(1)
            if(j == "-"):
                seql.append(-1)

        for j in xrange(len(seql)):
            if seql[j] == -1:
                for k in xrange(1, size):
                    if (j+k < len(seql)):
                        if (seql[j+k] == 1) :
                            if (j+size+k <= len(seql)) :
                                seql[j+k:j+k+size] = ret_minus(seql,j+k,size)
                                flag = flag+1
                            else:
                                flag = -1
                                break
                    else:
                         flag = -1
                if flag != -1 :
                    seql[j:j+size] = ret_minus(seql,j,size)
                    flag = flag+1
                else:
                    break
        if flag >= 0:
            print "Case #{}: {}".format(i,flag)
        else:
            print "Case #{}: IMPOSSIBLE".format(i)
