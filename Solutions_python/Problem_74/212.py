
def process(orders):
    b_targets = []
    o_targets = []
    b_position = 1
    o_position = 1
    for order in orders:
        if order[0] == 'B':
            b_targets.append(order[1])
        if order[0] == 'O':
            o_targets.append(order[1])
    ticks = 0
    while len(orders) != 0:
        ticks += 1
        order = orders[0]
        if order[0] == 'B':
            b_target = b_targets[0]
            if b_target > b_position: b_position += 1
            elif b_target < b_position: b_position -= 1
            else:
                orders.pop(0)
                b_targets.pop(0)
            if len(o_targets) == 0: pass
            else:
                o_target = o_targets[0]
                if o_target > o_position: o_position += 1
                elif o_target < o_position: o_position -= 1
                else:
                    pass
        if order[0] == 'O':
            o_target = o_targets[0]
            if o_target > o_position: o_position += 1
            elif o_target < o_position: o_position -= 1
            else:
                orders.pop(0)
                o_targets.pop(0)
            if len(b_targets) == 0: pass
            else:
                b_target = b_targets[0]
                if b_target > b_position: b_position += 1
                elif b_target < b_position: b_position -= 1
                else:
                    pass
    return ticks


fin = open('A-large.in', 'r')
fout = open('A-large.out', 'w')
t = int(fin.readline().rstrip())
for i in range(1, t+1):
    tokens = fin.readline().rstrip().split(' ')
    order_length = int(tokens.pop(0))
    orders = []
    for j in range(0,order_length * 2,2):
        orders.append((tokens.pop(0), int(tokens.pop(0))))
    fout.write( 'Case #%d: %d\n' %(i, process(orders)))
    
fin.close()
fout.close()

