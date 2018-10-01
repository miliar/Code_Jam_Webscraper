with open('in', 'r') as f:
    T = int(f.readline().strip())
    result = list()
    for i in range(T):
        N = f.readline().strip()
        N = list(map(int,list(N)))
        number = ''
        while len(N) > 1:
            n = N.pop()
            if n < 1 or n < N[-1]:
                number = '9'*(len(number)+1)
                N[-1] -= 1
            else:
                number = str(n) + number
        if N[0]:
            number = str(N[0]) + number

        result.append('Case #' + str(i+1)+': '+number+'\n')

with open('out', 'w') as f:
    for case in result:
        f.write(case)

