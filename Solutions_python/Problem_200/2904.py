def solve(n):
    n_len = len(str(n))
    if n_len == 1:
        return n
    else:
        result = []
        prev = int(str(n)[n_len-1]) #previous value
        result.insert(0, prev)
        for i in range(n_len-2, -1, -1): # 2nd last digit: first digit (inclusive)
            val = int(str(n)[i])
            if val > result[0]: #current val bigger than prev val?
                for j in range(0, len(result)): #all previous digits are now 9's
                    result[j] = 9
                result.insert(0, val-1)
            else:
                result.insert(0, val)

        return int(''.join(str(x) for x in result))




if __name__ == "__main__":
    test_case_num = raw_input()
    for i in range(1, int(test_case_num)+1):
        n = int(raw_input())
        result = solve(n)
        print("Case #" + str(i) + ": " + str(result))
