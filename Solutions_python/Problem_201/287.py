import heapq


INPUT_FILE = "./C-large.in"
OUTPUT_FILE = "./C-large.out"


class MaxHeap():
    def __init__(self):
        self.heap = []


    def push(self, x):
        heapq.heappush(self.heap, -x)


    def pop(self):
        return -heapq.heappop(self.heap)



def slove(n, k):
    ans_x, ans_y = n, n
    intervals = MaxHeap()
    intervals.push(n)
    while k > 0:
        k -= 1
        y = intervals.pop()
        if y & 1:
            ans_x = y // 2
            ans_y = ans_x
        else:
            ans_x = y // 2
            ans_y = ans_x - 1
        if ans_x > 0:
            intervals.push(ans_x)
        if ans_y > 0:
            intervals.push(ans_y)
    return ans_x, ans_y


if __name__ == '__main__':
    with open(INPUT_FILE, "r") as fin, open(OUTPUT_FILE, "w") as fout:
        T = int(fin.readline())
        for case_i in range(1, T + 1):
            n, k = map(int, (fin.readline().split()))
            x, i = 1, 0
            while k > x:
                k -= x
                x *= 2
                i += 1

            n -= 2 ** i - 1
            m = n // x
            reminder = n % x
            if k == 0:
                if reminder:
                    ans_x, ans_y = m + 1, m
                else:
                    ans_x, ans_y = m, m
            else:
                if k <= reminder:
                    m += 1
                if m & 1:
                    ans_x, ans_y = m // 2, m // 2
                else:
                    ans_x, ans_y = m // 2, m // 2 - 1

            print('Case #{}: {} {}'.format(case_i, ans_x, ans_y))
            print('Case #{}: {} {}'.format(case_i, ans_x, ans_y), file = fout)
