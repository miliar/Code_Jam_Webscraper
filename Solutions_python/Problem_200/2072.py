def generate_tidy(n):
    a = [int(i) for i in str(n)]
    backup = '9'*(len(a)-1)
    if backup == '':
        backup = '0'

    b = ''
    cat_9 = False
    for i in range(len(a)):
        if not cat_9:
            if min(a[i:]) != a[i]:
                cat_9 = True
                b = b + str(a[i] - 1)
            else:
                b = b + str(min(a[i:]))
        else:
            b = b + '9'    

    return max(int(backup), int(b))

def test_tidy(a):
    for i in range(len(a) - 1):
        if a[i + 1] < a[i]:
            return False
    return True



def good_generate_tidy(n):
    a = [int(i) for i in str(n)]

    if test_tidy(a):
        return n
    else:
        for i in range(len(a)):
            if test_tidy(a[:i+1]):
                continue
            else:
                tmp = a[:i]
                tmp[-1] = tmp[-1] - 1
                if tmp[-1] == -1:
                    return '9'*(len(str(n))-1)
                break
        print tmp
        b = ''.join([str(i) for i in tmp])
        while len(b) < len(str(n)):
            b = b + '9'
        return int(b)


def cat_to_n(s, n):
    # print("cat %s to %s" % (s, n))
    tmp = ''.join([i for i in s])
    val = tmp[-1]
    while len(tmp) < n:
        tmp = tmp + val
    # print("cat returning %s" % tmp)
    return tmp

def third_try(n):
    # print "running on %s" % n
    a = [int(i) for i in str(n)]
    if test_tidy(a):
        return n
    if int('1'*len(a)) > n:
        return int('9'*(len(a)-1))

    b = str(a[0])

    # print a
    # print b  
    for i in range(1,len(a)):
        candidate = cat_to_n(b, len(a))
        # print candidate
        if int(candidate) > n:
            final = [i for i in b]
            final[-1] = str(int(final[-1]) - 1)
            final.append('9')
            final = ''.join(final)
            final = cat_to_n(final, len(a))
            return final
        else:
            b = b + str(a[i])






if __name__ == '__main__':

    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
      n = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
      print "Case #{}: {}".format(i, third_try(n[0]))
      # check out .format's specification for more formatting options