def check_pa(xs):
    xl = len(xs)
    l = 0
    u = xl-1
    while l < u:
        if xs[l] != xs[u]:
            return False
        l += 1
        u -= 1
    return True
    
a_list = [1,4,9,121,484]

for i in range(1,10):
    for j in range(10):
        s = str(i)+str(j)+str(i)
        x = int(s)*int(s)
        xs = str(x)
        if check_pa(xs):
            a_list.append(x)

for i in range(1,10):
    for j in range(10):
        s = str(i)+str(j)+str(j)+str(i)
        x = int(s)*int(s)
        xs = str(x)
        if check_pa(xs):
            a_list.append(x)
            
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            s = str(i)+str(j)+str(k)+str(j)+str(i)
            x = int(s)*int(s)
            xs = str(x)
            if check_pa(xs):
                a_list.append(x)

for i in range(1,10):
    for j in range(10):
        for k in range(10):
            s = str(i)+str(j)+str(k)+str(k)+str(j)+str(i)
            x = int(s)*int(s)
            xs = str(x)
            if check_pa(xs):
                a_list.append(x)
                
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                s = str(i)+str(j)+str(k)+str(l)+str(k)+str(j)+str(i)
                x = int(s)*int(s)
                xs = str(x)
                if check_pa(xs):
                    a_list.append(x)

num = raw_input()
import sys
num_problem = 1
for line in sys.stdin:
    if len(line) < 2:
        continue
    nums = line.split()
    l_bound = int(nums[0])
    u_bound = int(nums[1])
    cnt = 0
    for num in a_list:
        if num < l_bound:
            continue
        elif num <= u_bound:
            cnt += 1
        else:
            break
    print "Case #" + str(num_problem) + ": " + str(cnt)
    num_problem += 1
        
