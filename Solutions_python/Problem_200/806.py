# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())  # read a line with a single integer
for k in xrange(1, t + 1):
    ans = raw_input()  # read a list of integers, 2 in this case
    ans = list(ans)
    ans = map(lambda x: int(x), ans)
    same = 0
    for i, el in enumerate(ans[1:]):
        if el > ans[i]:
            same = i + 1
        elif el < ans[i]:
            ans[same] -= 1
            for x in xrange(same + 1, len(ans)):
                ans[x] = 9
            break
    print "Case #{}: {}".format(k, int(''.join(map(str, ans))))
