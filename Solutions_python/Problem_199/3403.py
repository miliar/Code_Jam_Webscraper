import numpy as np
import queue

def n_primes(n):
    result = [2]
    i = 3

    while len(result) < n:
        flag = True

        for prime in result:
            if i % prime == 0:
                flag = False
                break

        if flag:
            result.append(i)

        i += 2
    return result

def run_pf_solver(filename):
    with open(filename, "r") as inpt:
        num_cases = int(next(inpt))

        for idx, test_case in enumerate(inpt):
            test_case_arr = test_case.split()

            pancakes = np.array([1 if a == '+' else 0 for a in test_case_arr[0]], dtype=np.uint8)
            flipper_size = int(test_case_arr[1])

            res = pf_solver(flipper_size, pancakes)

            print ("Case #%d: %s" % (idx + 1, str(res) if res != -1 else "IMPOSSIBLE"))

def pf_flipper(pancakes, c_from, c_to):
    new_pancakes = np.copy(pancakes)

    new_pancakes[c_from:c_to] += 1
    new_pancakes[c_from:c_to] %= 2

    return new_pancakes

def flip_hash(pancakes, hashV):
    return np.sum(pancakes *  hashV)

def pf_solver(flipper_size, pancakes):
    num_pancakes = len(pancakes)

    hashV = n_primes(num_pancakes)

    discovered_states = set()
    stack = queue.Queue()

    stack.put((0, pancakes))

    while not stack.empty():
        iteration, state = stack.get()

        if np.sum(state) == num_pancakes:
            return iteration

        for c_from in range(0, num_pancakes - flipper_size + 1):
            new_state = pf_flipper(state, c_from, c_from + flipper_size)
            new_state_hash = flip_hash(new_state, hashV)

            if new_state_hash not in discovered_states:
                discovered_states.add(new_state_hash)
                stack.put((iteration + 1, new_state))

    return -1


run_pf_solver("A-small-attempt0.in")