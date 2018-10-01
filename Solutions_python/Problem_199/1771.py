from itertools import product


def flip_one(pancake):
    return '+' if pancake == '-' else '-'


def flip(pancakes, start, count):
    return ''.join(
        [pancakes[i] if i < start or i >= start + count else flip_one(pancakes[i]) for i in range(0, len(pancakes))])


def is_ok(pancakes):
    for p in pancakes:
        if p == '-':
            return False
    return True


def choices(S, K):
    return product(range(2), repeat=S - K + 1)


def apply_choice(choice, pancakes, K):
    result = pancakes
    for start in range(len(choice)):
        if choice[start]:
            result = flip(result, start, K)
    return result


def choice_value(choice):
    return sum(choice)


def solve(pancakes, K):
    S = len(pancakes)
    K = int(K)
    best = S
    for choice in choices(S, K):
        if is_ok(apply_choice(choice, pancakes, K)):
            if sum(choice) < best:
                best = sum(choice)
    if best == S:
        return "IMPOSSIBLE"
    return best


if __name__ == "__main__":
    T = int(input())
    for I in range(1, T + 1):
        pancakes, K = input().split()
        print("Case #{}: {}".format(I, solve(pancakes, K)))
