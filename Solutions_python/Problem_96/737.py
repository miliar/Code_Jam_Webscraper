#!/usr/bin/env python3


def get_max_best_score(scores, nbr_surprise, p):
    # Any score in [inf_limit, sup_limit[ is a suprising score.
    inf_limit = max(p, (3*p - 4))
    # Any score in [sup_limit, infinity[ is an acceptable score.
    sup_limit = (3*p - 2)
    return (
        # Only nbr_surprise suprising scores are acceptable not more.
        min(
            nbr_surprise,
            len([i for i in scores if inf_limit <= i < sup_limit])
        ) +
        len([i for i in scores if i >= sup_limit])
    )



def main():
    n = int(input())
    for i in range(n):
        _, nbr_surprise, p, *scores = map(int, input().split())
        res = get_max_best_score(scores, nbr_surprise, p)
        print('Case #{:d}: {:d}'.format(i + 1, res))


if __name__ == '__main__':
    main()
