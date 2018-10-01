#coding=utf-8
#author=godpgf
import fileinput


def get_res(data, k):
    count = 0
    start_index = 0
    is_rev = False
    while start_index <= len(data) - k:
        start_index, is_rev = reveng_line(start_index, k, data)
        if is_rev:
            count += 1
    for i in range(len(data)-k,len(data)):
        if data[i] != '+':
            return 'IMPOSSIBLE'
    return str(count)


# 从start_index起找到第一个非+点，然后翻转连续k个饼，返回下次开始
def reveng_line(start_index, k, data):
    for i in range(start_index, len(data) - k + 1):
        if data[i] == '+':
            continue
        for j in range(0, k):
            data[i + j] = '-' if data[i + j] == '+' else '+'
        return i + 1, True
    return len(data) - k + 1, False

if __name__ == '__main__':
    input = fileinput.input('A-large.in')
    n = int(input.readline())
    for i in range(n):
        data = input.readline()[:-1]
        k = int(data.split(' ')[1])
        data = data.split(' ')[0]
        print "Case #%d: %s" % ((i + 1), get_res(list(data), k))