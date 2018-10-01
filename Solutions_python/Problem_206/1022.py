

def A():
    #with open('A-small-attempt0.in', 'r') as infile:
    with open('A-large.in', 'r') as infile:
    #with open('input.txt', 'r') as infile:
        with open('output.txt', 'w') as outfile:
            T = int(infile.readline().strip())
            for t in range(T):
                line = infile.readline().split()
                D = int(line[0])
                N = int(line[1])

                max_speed = -1
                for n in range(N):
                    line = infile.readline().split()
                    K = int(line[0])
                    S = int(line[1])
                    if max_speed < 0:
                        max_speed = D / (float(D-K) / S)
                    else:
                        max_speed = min(D / (float(D-K) / S), max_speed)

                outfile.write('Case #%d: %.06f\n' % (t+1, max_speed))
