__author__ = 'Shih-Ting Huang'

"""
2017 Google Code Jam
Author: Shih-Ting Huang
"""


def tidy_number(n):
    num_str = list(str(n))
    if len(num_str) <= 1:
        return n
    for i in range(len(num_str)-2, -1, -1):
        if int(num_str[i]) > int(num_str[i+1]):
            for j in range(i+1, len(num_str)):
                num_str[j] = '9'
            num_str[i] = str(int(num_str[i]) - 1)
    result = ''
    for x in num_str:
        result += x
    return int(result)


def main():
    caseNum = int(input())
    with open("Output.txt", "w") as text_file:
        for i in range(1, caseNum+1):
            num = int(input())
            result = tidy_number(num)
            print("Case #{}: {}".format(i, result), file=text_file)


if __name__ == '__main__':
    main()