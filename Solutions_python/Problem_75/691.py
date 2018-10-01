import sys

lines = sys.stdin.readlines()
lines = map(lambda a:a.rstrip('\n'), lines)
#print lines

N = int(lines[0])
for i in range(N):
    data = lines[i+1].split()

    C = int(data[0])
    combine_dict = {}
    for j in range(C):
        d = data[j+1]
        k = d[0:2]
        v = d[2]
        combine_dict[k] = v
        
        
    D = int(data[C+1])
    oppose_list = []
    for j in range(D):
        d = data[C+2+j]
        oppose_list.append(d)
    
    N = int(data[C+D+2])
    s = data[C+D+3]
    
    m = ''
    for c in s:
        m += c
        if len(m)<2:
            continue
        
        # combine
        while True:
            if len(m)<2:
                break
            last2 = m[-2:]
            last22 = m[-1]+m[-2]
            if last2 in combine_dict.keys():
                m = m[:-2]
                m += combine_dict[last2]
            elif last22 in combine_dict.keys():
                m = m[:-2]
                m += combine_dict[last22]
            else:
                break
        if len(m)<2:
            continue    
        
        # oppose
        k1 = m[-1]
        for oppose in oppose_list:
            if len(m)<2:
                break
            if not k1 in oppose:
                continue
            
            if k1==oppose[0]:
                k2 = oppose[1]
            else:
                k2 = oppose[0]
            index = None
            for k in range(len(m)):
                if m[k]==k2:
                    index = k
                    break
            if index!=None:
                m = ''#m[0:index]
    
    ans = ''
    for j in range(len(m)):
        if j==len(m)-1:
            ans += m[j]
        else:
            ans += m[j]+', '
            
    print 'Case #%d: [%s]' % (i+1, ans)
        