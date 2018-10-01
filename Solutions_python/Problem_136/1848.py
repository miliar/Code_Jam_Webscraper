def solve(C,F,X):
    time_elapsed = 0.0
    time_to_win = X/2.0
    income = 2.0
    while True:
        time_to_buy_farm = C/(income)
        time_to_win_with_newfarm = X/(income+F)
        if (time_to_win<=time_to_buy_farm+time_to_win_with_newfarm):
            break
        time_to_win = time_to_win_with_newfarm
        income += F
        time_elapsed += time_to_buy_farm
    return time_elapsed+time_to_win

with open('B-large.in', 'r') as f:
    inp = f.readlines()
    f.close()
#inp = raw_input().split('\n')
line_counter = 0
T = int(inp[line_counter])
line_counter+=1
data = ''
for i in range(T):
    cfx = inp[line_counter].split(' ')
    line_counter+=1
    #print float(cfx[0]),float(cfx[1]),float(cfx[2])
    data += 'Case #%d: %.7f\n' %(i+1, solve(float(cfx[0]), float(cfx[1]), float(cfx[2])))
with open('output.txt', 'w') as f:
    f.write(data)
    f.close()
print data
