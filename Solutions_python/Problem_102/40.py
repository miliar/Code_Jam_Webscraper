def wins(X, p, i, scores):
    X = float(X)
    total_added = 0
    for j, s in enumerate(scores):
        if j == i:
            continue
        if s <= scores[i]+X*p:
            total_added += ((scores[i] + X*p - s)/X)
    if total_added + p >= 1:
        return True
    return False


def solve(scores):
    X = sum(scores)
    results = []
    for i, s in enumerate(scores):
        pmax = 1.
        pmin = 0.
        p = (pmax + pmin)/2
        last_p = -1
        while True:
            if wins(X, p, i, scores):
                pmax = p
            else:
                pmin = p
            p = (pmax+pmin)/2
            if abs(p-last_p) <= 10**-9:
                break
            last_p = p
        results.append(round(p*100, 6))

    return results

if __name__=="__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        scores = map(int, raw_input().split())[1:]
        results = solve(scores)
        print "Case #%d:" % i, " ".join(map(str, results))
    
