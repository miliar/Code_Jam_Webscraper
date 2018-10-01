__author__ = 'valeria'


def get_test():
    s = input().split()
    l = [int(x) for x in s[1]]
    return l




def get_tests():
    n = int(input())
    tests = []
    for i in range(n):
        tests.append(get_test())
    return tests


def f_invite(test):
    people = 0
    new_fr = 0
    for index, x in enumerate(test):
        if people < index:
            new_fr += index - people
            people += index - people
        people += x
    return new_fr


def main():
    tests = get_tests()
    for index, test in enumerate(tests):
       print("Case #{}: {}".format(index + 1, f_invite(test)))



if __name__ == '__main__':
    main()