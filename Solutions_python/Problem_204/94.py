T = int(input())

for t in range(1, T+1):
    N, P = [int(x) for x in input().split()]
    recipe = [int(x) for x in input().split()]
    quant = []
    for n in range(N):
        quant.append(sorted([int(x) for x in input().split()], reverse=True))

    n_good = 0 
    while True:
        curr_set = [l[-1] for l in quant]
        frac = [curr_set[j] / recipe[j] for j in range(N)]
        min_frac = min(frac)
        i = int(0.89 * min_frac)
        if i < 1:
            i = 1
        least_i = -1
        least_pen = 0
        while True:
            frac = [curr_set[j] / (recipe[j] * i) for j in range(N)]
            if max(frac) < 0.9:
                break

            good = True
            for j in range(N):
                if frac[j] < 0.9 or frac[j] > 1.1:
                    pen = 0
                    for f in frac:
                        if f < 0.9:
                            pen += 0.9 - f
                        elif f > 1.1:
                            pen += f - 1.1
                    if least_i == -1 or pen < least_pen:
                        least_i = i
                        least_pen = pen
                    good = False
                    break
            if good:
                n_good += 1
                break
            i += 1
        
        if good:
            quant = [l[:-1] for l in quant]
            min_len = min([len(l) for l in quant])
            if min_len == 0:
                break
        else:
            frac = [curr_set[j] / (recipe[j] * least_i) for j in range(N)]
            min_idx = -1
            min_val = 0
            for k, f in enumerate(frac):
                if min_idx == -1 or f < min_val:
                    min_val = f
                    min_idx = k
            quant[min_idx] = quant[min_idx][:-1]
            if len(quant[min_idx]) == 0:
                break
    print(f'Case #{t}: {n_good}')
