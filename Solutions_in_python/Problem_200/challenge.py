def counting(n):
    tidy_numbers = []
    n = int(n)
    for i in range(1, n+1):
        if ''.join(sorted(str(i))) == str(i) and str(i)[0] != '0':
            tidy_numbers.append(i)
    return tidy_numbers[-1]

files = open('bsmall.in', 'r')
data = open('results.txt', 'w')
lista = files.read().strip().split('\n')
results = [counting(i) for i in lista]
counter = 1
for i in range(len(results)):
    data.write('Case #{}: '.format(counter) + str(results[i])+'\n')
    counter += 1
