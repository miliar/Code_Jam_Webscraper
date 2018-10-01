'''
Google Code Jam 2017 Qualification Round
Problem C. Bathroom Stalls
Solution by Liu Yue <euyuil@gmail.com>
Created at 2017-04-09T00:10:00+0800
'''
import heapq

def calc2(stall_num, person_num):
    '''
    Calculate the max(l, r) and the min(l, r).
    '''
    heap = [-stall_num]
    for _ in range(0, person_num):
        last_deq = -heapq.heappop(heap)
        left = int((last_deq - 1) / 2)
        right = last_deq - left - 1
        if left > 0:
            heapq.heappush(heap, -left)
        if right > 0:
            heapq.heappush(heap, -right)
    return right, left

def calc(stall_num, person_num):
    '''
    Calculate the max(l, r) and the min(l, r).
    '''
    arr = [False] * (stall_num + 2)
    arr[0] = True
    arr[-1] = True
    max_maxlr = -1
    max_minlr = -1
    for _ in range(0, person_num):
        left = 0
        right = 0
        pos = -1
        max_maxlr = -1
        max_minlr = -1
        for i in range(1, stall_num + 1):
            if arr[i]:
                left = 0
                right = 0
                continue
            if right <= 0:
                right = arr.index(True, i+1) - i - 1
            maxlr = max(left, right)
            minlr = min(left, right)
            if minlr > max_minlr:
                pos = i
                max_minlr = minlr
                max_maxlr = maxlr
            elif minlr == max_minlr and maxlr > max_maxlr:
                pos = i
                max_maxlr = maxlr
            left = left + 1
            right = right - 1
        arr[pos] = True
    return max_maxlr, max_minlr

def main():
    '''
    The main method for the program.
    '''
    with open('C-small-1-attempt1.in') as fin, open('C-small-1-attempt1.out', 'w') as fout:
        fin.readline()
        curr = 1
        for line in fin:
            parts = line.split(' ')
            maxlr, minlr = calc2(int(parts[0]), int(parts[1]))
            fout.write('Case #%d: %d %d\n' % (curr, maxlr, minlr))
            curr = curr + 1

if __name__ == '__main__':
    main()
