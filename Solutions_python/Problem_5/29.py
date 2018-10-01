INPUT = 'B-small-attempt0.in'
OUTPUT = INPUT.replace('.in', '.out')

f = open(INPUT, 'r')
input = f.readlines()
f.close()
N = eval(input[0])
input = input[1:]

f = open(OUTPUT, 'w')

case = 0
i = 0
while case < N:
    customers = []
    case += 1
    num_flavors = eval(input[i].strip())
    i += 1
    num_customers = eval(input[i].strip())
    i += 1
    for j in xrange(num_customers):
        data = input[i + j].strip().split(' ')
        for k in xrange(len(data)):
            data[k] = eval(data[k])
        num = data[0]
        data = data[1:]
        tmp_customer = []
        for k in xrange(num):
            tmp_customer.append((data[2*k], data[2*k+1]))
        customers.append(tmp_customer)
    i += num_customers
    j = 0
    while j < (2 ** num_flavors):
        try:
            for c in customers:
                found_match = False
                for t in c:
                    t_mask = 1 << (t[0] - 1)
                    if (bool(j & t_mask) == bool(t[1])):
                        found_match = True
                        break
                if not found_match:
                    raise Exception
            break
        except:
            None
        j += 1
    if j == 2 ** num_flavors: # no answer - IMPOSSIBLE
        print 'Case #%d: IMPOSSIBLE' % case
        f.write('Case #%d: IMPOSSIBLE\n' % case)
        continue
    k = 0
    res = []
    for k in xrange(num_flavors):
        if ((1 << k) <= j) and (j & (1 << k)):
            res.append(1)
        else:
            res.append(0)
        k += 1
    answer = ''
    for r in res:
        answer += ' %d' % r
    print 'Case #%d:%s' % (case, answer)
    f.write('Case #%d:%s\n' % (case, answer))
    
f.close()
