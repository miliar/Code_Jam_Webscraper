import re
T = int(input())
for n in range(T):
    R = input().strip().split(' ')
    R, C = int(R[0]), int(R[1])
    co = []
    region = {}
    has_d = False
    hasd = []
    for i in range(R):
        co.append(input().strip())
        resp = re.findall('[A-Z]', co[i])
        if '?' in co[i]:
            has_d = True
            hasd.append(i)
        if resp:
            for z in resp:
                if z not in region:
                    region[z] = {}
                    region[z]['min_lin'] = i
                    region[z]['min_col'] = co[i].index(z)
                    region[z]['max_lin'] = i
                    region[z]['max_col'] = co[i].index(z)
                else:
                    if i > region[z]['max_lin']:
                        region[z]['max_lin'] = i
                    if co[i].index(z) > region[z]['max_col']:
                        region[z]['max_col'] = co[i].index(z)

    for i in range(R):
        if not has_d:
            break
        if i not in hasd:
            continue
        size = len(co[i])
        for j in range(size):
            if co[i][j] == '?':
                for z in region:
                    ok = True
                    max_lin = 0
                    max_col = 0
                    min_lin = 0
                    min_col = 0
                    if i > region[z]['max_lin']:
                        max_lin = i
                    else:
                        max_lin = region[z]['max_lin']
                    if j > region[z]['max_col']:
                        max_col = j
                    else:
                        max_col = region[z]['max_col']
                    if j < region[z]['min_col']:
                        min_col = j
                    else:
                        min_col = region[z]['min_col']
                    if i < region[z]['min_lin']:
                        min_lin = i
                    else:
                        min_lin = region[z]['min_lin']
                    for r in region:
                        if not ok:
                            break
                        if r == z:
                            continue
                        for x in range(min_lin,max_lin+1):
                            if ok:
                                for y in range(min_col, max_col+1):
                                    if x <= region[r]['max_lin'] and x >= region[r]['min_lin'] and y >= region[r]['min_col'] and y <= region[r]['max_col']:
                                        ok = False
                                        break
                            else:
                                break
                    if ok:
                        co[i] = co[i][:j] + z + co[i][j+1:]
                        if i > region[z]['max_lin']:
                            region[z]['max_lin'] = i
                        if j > region[z]['max_col']:
                            region[z]['max_col'] = j
                        if j < region[z]['min_col']:
                            region[z]['min_col'] = j
                        if i < region[z]['min_lin']:
                            region[z]['min_lin'] = i
                        break
                
    print("Case #{}:".format(n+1))
    for i in range(R):
        print(co[i])
        
