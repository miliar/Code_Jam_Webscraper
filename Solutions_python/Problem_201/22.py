
def bathroom_stalls_solve(N, K):
    if K == N:
        return (0, 0)
    if K == 1:
        if N % 2 == 1:
            return ((N - 1) / 2, (N - 1) / 2)
        else:
            return ((N + 1) / 2, (N - 1) / 2)

    if N % 2 == 1:
        return bathroom_stalls_solve((N - 1) / 2, K / 2)
    else:
        if K % 2 == 0:
            return bathroom_stalls_solve((N + 1) / 2, K / 2)
        else:
            return bathroom_stalls_solve((N - 1) / 2, (K - 1) / 2)
         
def bathroom_stalls_main(input_filename, output_filename):
    f = open(input_filename, "rb")
    output_f = open(output_filename, "w")
    
    T = int(f.readline().split()[0])
    for i in range(1, T + 1):
        N, K = [int(x) for x in f.readline().split()]               
        max_dist, min_dist = bathroom_stalls_solve(N, K)
        #print N, K, max_dist, min_dist
        
        output_f.write("Case #" + str(i) + ": " + str(max_dist) + " " + str(min_dist) + "\n")
    return 1

bathroom_stalls_main("C-large.in", "C-large.out")
