def is_tidy(n):
    A = list(str(n))
    for i in range(0, len(A) - 1):
        if A[i] > A[i+1]:
            return False
    return True
def inv_point(n):
    A = list(str(n))
    for i in range(0, len(A) - 1):
        if A[i] >= A[i+1]:
            return i
    return n

if __name__ == '__main__':
    t = int(input().strip())
    for tests in range(1, t + 1):
        s = input().strip()
        n = int(s)
        if is_tidy(n):
            a = n
        else:
            A = list(map(int, s))
            g = 9
            b = ''
            B = [x for x in A]
            j = inv_point(n)
            i = len(A) - 1
            carry = A[i] < 9
            A[i] = 9
            i -= 1
            while i >= 0:
                if carry:
                    A[i] -= 1
                    if A[i] == -1:
                        A[i] = 0
                    else:
                        carry = False
                if i > j:
                    carry = A[i] < 9
                    A[i] = 9
                i -= 1
            a = int(''.join([str(x) for x in A]))
        print("Case #{test}: {ans}".format(test=tests, ans=a))