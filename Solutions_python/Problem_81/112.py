def getOOWP(k, record):
    n=0
    tot=0
    for i in range(len(record[k])):
        if i==k:
            continue
        
        game = record[k][i]
        if game!='.':
            tot += getOWP(i, record)
            n+=1

    return tot/n

def getOWP(k, record):
    n = 0
    tot = 0
    for i in range(len(record[k])):
        if i==k:
            continue

        game = record[k][i]
        if game!='.':
            tot += getWP(i, record, exclude=[k])
            n+=1

    return tot/n


def getWP(k, record, exclude=[]):
    ws = 0
    ls = 0
    for i in range(len(record[k])):
        if i in exclude:
            continue

        game = record[k][i]
        if game=='1': ws+=1
        elif game=='0': ls+=1

    return ws/(ws+ls)


def getRPI(k, record):
    return .25*getWP(k, record) + .5*getOWP(k, record) + .25*getOOWP(k, record)


f = open('input.in', 'r')
i = 0
lines = f.readlines()
T = int(lines[i])
i+=1

for caseNum in range(T):
    N = int(lines[i])
    i+=1
    record = []
    for j in range(N):
        line = lines[i].strip()
        i += 1
        record.append(list(line))
    
    print('Case #'+(str(caseNum+1)+':'))
    for k in range(len(record)):
        print(getRPI(k, record))
