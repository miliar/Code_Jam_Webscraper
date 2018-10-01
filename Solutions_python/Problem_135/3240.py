def solve(testNum):
    cards = set((i + 1) for i in range(16))
    for it in range(2):
        num = int(raw_input())
        for i in range(4):
            nums = map(int, raw_input().split())
            if i == num - 1:    
                cards &= set(nums)
    ans = ""
    if len(cards) < 1:
        ans = "Volunteer cheated!"
    elif len(cards) > 1:
        ans = "Bad magician!"
    else:
        ans = list(cards)[0]
    print "Case #%s: %s" % (testNum, ans,)

    
t = int(raw_input())
for i in range(t):
    solve(i + 1)
        
