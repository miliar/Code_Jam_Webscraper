

def get_n(k):
    tot=0
    n=0
    while tot < k:
        tot += 2**n
        n+=1
    return n-1

def get_sum(n):
    tot = 0
    for i in range(n+1):
        tot += 2**i
    return tot

def get_max_min(j):
    div = (j-1)/2.0
    min = round(div) - 1 if round(div)>div else div
    max = round(div)
    return str(int(max)) + ' ' + str(int(min))

if __name__ == "__main__":
    with open('/home/roberta/Documenti/gcj/B_small.txt', 'r') as filein:
        lines = filein.readlines()
        output = open('/home/roberta/Documenti/gcj/output3.txt', 'w')
        for p, line in enumerate(lines[1:]):
            numbers = line.split()
            N = int(numbers[0])
            k = int(numbers[1])
            n = get_n(k)
            A = N - get_sum(n-1)
            max = A/(2.0**n)
            if max != round(max):
                max = round(max) + 1 if round(max) < max else round(max)
                n_min = (max * (2.0**n)) - A
                n_max = 2.0**n - n_min
                remaining = k - get_sum(n-1) # da piazzare nell ultimo scaglione
                if remaining <= n_max:
                    res = get_max_min(max)
                else:
                    res = get_max_min(max-1)
            else:
                max = round(max)
                res = get_max_min(max)

            output.write('Case #' + str(p + 1) + ': ' + res + '\n')