def is_tidy(n):
    s = str(n)

    for i in range(len(s)-1, 0, -1):
        if s[i-1] > s[i]:
            return False
    return True


def second():
    t = int(input())
	
    for i in range(t):
        n = int(input())

        if n < 10 or is_tidy(n):
            print("Case #" + str(i+1) + ":", n)
        else:
            s = list(map(int, list(str(n))))
            largest = 0
            start = end = 0

            for j in range(1, len(s)):
                if s[j-1] == s[j]:
                    end += 1
                else:
                    if s[j-1] > s[j]:
                        largest = start
                        break
                    start = end = j

            if s[largest] == 1 and largest == 0:
                print("Case #" + str(i+1) + ":", "9" * (len(s)-1))
            else:
                s[largest] -= 1
                for k in range(largest+1, len(s)):
                    s[k] = 9
                print("Case #" + str(i+1) + ": ", *s, sep="")
second()


