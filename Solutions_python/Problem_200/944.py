import sys


class Solution:
    def find_tidy(self, n):
        s = str(n)
        length = len(s)
        t = ""
        for i in range(length):
            t += '1'
        if int(t) > n:
            return self.gen_max(length - 1)

        for i in range(length):
            while True:
                new_number = self.gen_new_number(t, i, length)
                if int(new_number) <= n:
                    t = new_number
                else:
                    break

        return t

    def gen_max(self, length):
        result = ""
        for i in range(length):
            result += '9'

        return int(result)

    def gen_new_number(self, number, i, length):
        result = ""
        for j in range(i):
            result += number[j]

        for j in range(i, length):
            result += str(int(number[i]) + 1)
        return result


# s = Solution()
# print s.find_tidy(132)

t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())
    solution = Solution()
    result = solution.find_tidy(n)
    print "Case #{}: {}".format(i, result)
