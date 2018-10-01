unique = [{'Z': 0, 'X': 6, 'W': 2, 'U': 4}, {'S': 7, 'R': 3, 'F': 5, 'O': 1},
          {'H': 8, 'N': 9}]
nums = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

[cases] = [int(x) for x in raw_input().strip().split()]
out = open('output.txt', 'w')

for case in range(cases):
    # solving logic goes here
    (p, k) = raw_input().strip().split()
    p = [1 if c == '+' else 0 for c in p]
    k = int(k)
    flips = 0

    for i in range(len(p) - k + 1):
        if (p[i] == 0):
            flips += 1
            for j in range(i, i+k):
                p[j] ^= 1

    # print and write output
    if all(p):
        ans = str(flips)
    else:
        ans = "IMPOSSIBLE"
    s = "Case #"+str(case+1)+": "+ans+'\n'
    out.write(s)
    print(s)
