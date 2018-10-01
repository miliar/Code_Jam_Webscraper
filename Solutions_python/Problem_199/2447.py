

def func_a():
    test_cases = int(raw_input())

    for case in xrange(1, test_cases + 1):
        # change from ints if different type
        line = raw_input().split(" ")
        k = int(line[1])
        line = line[0]
        method(line, k, case)

def method(line, k, case):
        count = 0


        orig_line = line
        if line[-1] == '+':
            line = line[::-1]

        if len(line) == k:
            if line.count('-') == k:
                count = 1
                line = reverseNextK(line)

        for i in xrange(0, len(line) - k +1):

            if line[i] == '+':
                pass
            else:
                reversed = reverseNextK(line[i:(i + k)])

                line = '%s%s%s' % (line[:i], reversed, line[(i + k):])

                if len(line)!= len(orig_line):
                    raise Exception(orig_line)
                count = count + 1

        if line.count('-') == 0:
            print "Case #%s: %s" % (case, count)
        else:
            print "Case #%s: %s" % (case, "IMPOSSIBLE")

def reverseNextK(subsequence):
    output = ""
    for i in subsequence:
        if i == '+':
            output = '%s%s' % (output, '-')
        else:
            output = '%s%s' % (output, '+')
    return output


func_a()
#method('+++--+', 2, 0)