# Tidy Numbers

def is_tidy(n):
    tidy = True
    digits = str(n)
    for d in range(len(digits) - 1):
        if digits[d] > digits[d + 1]:
            tidy = False
    return tidy

def brute_force_check(n):
    while(not is_tidy(n)):
        n -= 1
    return n

def correct_last_wrong_ordering(N):
    digits = list(map(int, str(N)))

    # Find idx up to which ordering is correct
    cor_order_idx = 0

    while(digits[cor_order_idx] <= digits[cor_order_idx + 1]):
        cor_order_idx += 1
        if (cor_order_idx + 1) == len(digits):
            # Reached the end
            break

    # Fix the ordering and maximize number
    digits[cor_order_idx] -= 1
    for i in range(cor_order_idx + 1, len(digits)):
        digits[i] = 9

    return int("".join(map(str, digits)))

def main():
    # Read in input
    num_test_case = int(input())

    for test_case in range(num_test_case):
        N = int(input())
        digits = list(map(int, str(N)))

        if len(digits) == 1:
            print_solution(test_case, str(N))
            continue

        sol = N
        while(not is_tidy(sol)):
            sol = correct_last_wrong_ordering(sol)

        # Remove leading zeroes
        sol = str(int(sol))
        #if int(sol) != brute_force_check(N):
            #print(N, sol, brute_force_check(N))
        print_solution(test_case, sol)

def print_solution(case_number, solution_string):
    print("Case #{}: {}".format(case_number + 1, solution_string))

if __name__ == "__main__":
    main()
