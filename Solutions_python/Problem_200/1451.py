N = int(input())

for test in range(N):
    s = list(input())
    sz = len(s)
    
    s.append("9")
    ans = ["9"] * sz

    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            if s[i] == "1":
                ans = list((sz - 1) * "9")
                break
            ans[i] = str(int(s[i]) - 1)
            
            j = i
            while j > 0 and ans[j] < ans[j-1]:
                ans[j] = "9"
                ans[j-1] = str(int(ans[j-1]) - 1)
                j -= 1

            break
        else:
            ans[i] = s[i]

    print("Case #" + str(test+1) + ":", end=" ")
    print("".join(ans))
