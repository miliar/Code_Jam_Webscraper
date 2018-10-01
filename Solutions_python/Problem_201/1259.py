# Bathroom
from math import log, floor, ceil

def get_child(n):
    tmp = n - 1
    #if tmp == 0:
#        return [0, 0]
    if tmp % 2 == 0:
        return [tmp // 2, tmp // 2]
    else:
        return [tmp // 2, (tmp // 2) + 1]

def solve_with_tree(N, K):
    if N == 1:
        return "0 0"

    #if K > ceil(N / 2):
    #    return "0 0"

    layer = int(floor(log(K, 2)))

    # Compute possible entries for each layer
    poss_minmax = [{N}]
    for i in range(1, layer + 2):
        poss_entries = set()
        for entry in poss_minmax[i - 1]:
            if ((entry - 1) % 2 == 0):
                # Only one option
                poss_entries.add(entry // 2)
            else:
                # Both possible
                poss_entries.add(entry // 2 - 1)
                poss_entries.add(entry // 2)
        poss_minmax.append(poss_entries)

    # Figure out whether we get a good position or not
    current_layer = list(poss_minmax[layer])

    # Find correct entry in layer k
    position_in_layer = K - 2**layer

    min_sol = 2**layer - 1 - (N % 2**layer)
    max_sol = 2**layer - min_sol

    tmp_sol = []
    if position_in_layer < max_sol:
        # Choose better option
        tmp_sol = get_child(max(current_layer))
    else:
        tmp_sol = get_child(min(current_layer))

    sol = "{} {}".format(max(tmp_sol), min(tmp_sol))
    return sol

def simulate_stupid(N, K):
    stalls = [0 for i in range(N)]
    stalls = [1] + stalls + [1]

    last_ls = -1
    last_rs = -1

    for k in range(K):
        # Compute LS / RS new
        ls = [N for i in range(N + 2)]
        rs = [N for i in range(N + 2)]
        for i in range(1, N + 1):
            if stalls[i] == 1:
                continue
            l = i
            r = i
            while(stalls[l] != 1):
                l -= 1
            while(stalls[r] != 1):
                r += 1
            ls[i] = i - 1 - l
            rs[i] = r - 1 - i

        best_v = 0
        best_indices = []
        for i in range(1, N + 1):
            if stalls[i] == 1:
                continue
            if min(ls[i], rs[i]) > best_v:
                best_v = min(ls[i], rs[i])
                best_indices = [i]
            elif min(ls[i], rs[i]) == best_v:
                best_indices.append(i)

        # Find max of ls/rs
        best_v = -1
        best_index = -1
        for i in best_indices:
            if max(ls[i], rs[i]) > best_v:
                best_v = max(ls[i], rs[i])
                best_index = i

        stalls[best_index] = 1
        last_ls = ls[best_index]
        last_rs = rs[best_index]
    return "{} {}".format(max(last_rs, last_ls), min(last_rs, last_ls))



def main():
    # Read in input
    num_test_case = int(input())

    for test_case in range(num_test_case):
        N, K = list(map(int, input().split()))
        #sol_sim = simulate_stupid(N, K)
        sol = solve_with_tree(N, K)
        #if sol_sim != sol:
        #    print(N, K, sol_sim, sol)
        print_solution(test_case, sol)




def print_solution(case_number, solution_string):
    print("Case #{}: {}".format(case_number + 1, solution_string))

if __name__ == "__main__":
    main()
