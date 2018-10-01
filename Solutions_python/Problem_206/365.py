t = int(input())

for i in range(t):
    s = input().split(" ")
    d = int(s[0])
    n = int(s[1])
    current = 0.0
    for _ in range(n):
        s = input().split(" ")
        remaining = d - int(s[0])
        speed = int(s[1])
        time = remaining/speed
        current = max(time, current)
    
    print("Case #{}: {}".format(i+1, d/current))