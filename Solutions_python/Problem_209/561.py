#!/usr/bin/env python3

from math import pi


def edge_area(cake):
    return 2 * cake[0] * pi * cake[1]


def top_area(cake):
    return pi * cake[0]**2


def diff(other, widest_in_stack, least_edge):
    top_diff = top_area(other) - top_area(widest_in_stack)
    edge_diff = edge_area(other) - edge_area(least_edge)

    return top_diff + edge_diff


num_cases = int(input())

for case in range(1, num_cases+1):
    num_cakes, stack_size = map(int, input().split())

    cakes = [tuple(map(int, input().split())) for x in range(num_cakes)]
    cakes.sort(key=edge_area, reverse=True)
    widest = max(cakes, key=top_area)

    stack = cakes[:stack_size]
    widest_in_stack = max(stack, key=top_area)
    least_edge = min(stack, key=edge_area)

    other_cakes = cakes[stack_size:]

    if other_cakes:
        best_other = max(other_cakes, key=lambda cake: diff(cake,
                                                            widest_in_stack,
                                                            least_edge))

        if diff(best_other, widest_in_stack, least_edge) > 0:
            stack.remove(least_edge)
            stack.append(best_other)

    exposed_area = (top_area(max(stack, key=top_area)) +
                    sum(edge_area(v) for v in stack))

    print("Case #{case}: {answer:.6f}".format(case=case, answer=exposed_area))
