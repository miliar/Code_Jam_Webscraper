import math

def is_palindrome(word):

    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])


def is_square(num):
    max_possibility = math.sqrt(num)
    for x in xrange(int(max_possibility) + 1):
        if x**2 == num:
            return x       

    return None



def main():
    num_test_cases = int(raw_input())
    for case in xrange(num_test_cases):

        raw_test = raw_input()
        bounds = [int(bound.strip()) for bound in raw_test.split(' ')]

        count = 0
        for num in xrange(bounds[0], bounds[1]+1):
            if is_palindrome(str(num)):
                root = is_square(num)
                if root:
                    if is_palindrome(str(root)):
                        count += 1

        print 'Case #{}: {}'.format(case+1, count)


if __name__ == '__main__':
    main()
