def pairs(num):
    num_str = str(num)
    res = []
    for i in range(len(num_str)):
        num_str = num_str[1:]+num_str[0]
        if num_str[0] != '0':
            res.append(int(num_str))
    return res
    
def recycled(s,e):
    recycled_num = 0
    full = range(s,e+1)
    p_set = []
    for i in full:
        for p in pairs(i):
            if s<=p and p<i and i<=e:
                recycled_num += 1
                p_set.append((i,p))
    return len(set(p_set))
          
f = open('C-small-attempt0.in')
f_out = open('C-small-attempt0.out','w')
num_of_cases = int(f.readline())
for i in range(1,num_of_cases+1):
    s = f.readline()
    numbers = [int(x) for x in s.split()]
    start = numbers[0]
    end = numbers[1]
    result = recycled(start,end)
    res = 'Case #%d: %s\n' % (i,result)
    f_out.write(res)
f.close()
f_out.close()
