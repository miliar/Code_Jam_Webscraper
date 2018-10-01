with open('B-large.in', 'r') as f:
    tasks = [l.strip() for l in f.readlines()[1:]]

for task_idx, num in enumerate(tasks):
    while True:
        faulty_idx = -1
        for i in range(len(num)-1):
            if int(num[i+1]) < int(num[i]):
                faulty_idx = i
                break
        if faulty_idx < 0:
            break
        if faulty_idx == 0:
            num = int(str(int(num[0])-1) + (len(num)-1)*'9')
            break
        num = ''.join([
            num[:faulty_idx],
            str(int(num[faulty_idx])-1),
            len(num[faulty_idx+1:])*'9'
        ])
    print 'Case #{}:'.format(task_idx+1), num
