import sys
import functools as ft
import itertools as it

best_so_far = None
def solve(case):
  global best_so_far 
  pancakes = sorted(case,reverse=True)
  best_so_far = pancakes[0]
  for solution in simulate(pancakes, 0):
    if solution < best_so_far:
      best_so_far = solution
  return best_so_far

# just try all the factors up to sqrt(1000)
try_factors=[2,3,5,7,11,13,17,19,23,27,29,31]

def split_max_stack(max_pancake, sorted_pancakes, factor):
  new_stack_size = max_pancake // factor
  stacks_with_extra = max_pancake % factor
  sorted_pancakes += [new_stack_size] * (factor - stacks_with_extra)
  sorted_pancakes += [new_stack_size + 1] * (stacks_with_extra)
  sorted_pancakes.sort(reverse=True)
  return sorted_pancakes

def simulate(sorted_pancakes, moves_so_far):
  if moves_so_far > best_so_far:
    return
  yield sorted_pancakes[0] + moves_so_far
  for factor in try_factors:
    if (factor - 1) > (sorted_pancakes[0] // factor):
      return
    next_pancakes = split_max_stack(sorted_pancakes[0], sorted_pancakes[1:], factor)
    yield next_pancakes[0] + moves_so_far + (factor - 1)
    for solution in simulate(next_pancakes, moves_so_far + factor - 1):
      yield solution
