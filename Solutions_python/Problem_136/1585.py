f = open("../../../../B-large.in", "r")
# f = open("../test.txt")
w = open("../../../../B-large.out", "w")
T = int(f.readline())

for i in range(1, T + 1):
    w.write("Case #" + str(i) + ": ")
    fac_cost, gain, goal = map(float, f.readline().split())
    cur_rate = 2.
    best = 1000000.
    time_taken = 0
    while True:
        cur_time = goal / cur_rate + time_taken
        # print cur_time
        if cur_time >= best:
            break
        best = cur_time
        time_taken += fac_cost / cur_rate
        cur_rate += gain
    w.write(str(best) + "\n")
        
    
    
