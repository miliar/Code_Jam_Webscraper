import math
import sys

def compute_sol_cost(sets, solution):
  cost = 0
  for i in range(len(sets)):
    for j in range(i + 1, len(sets)):
      if solution[i] == solution[j]:
        cost += sets[i][0] * sets[j][1]
        cost += sets[i][1] * sets[j][0]
  return cost

def get_next_sol(sets, solution):
  infeasible = True
  while infeasible:
    infeasible = False
    max_inc = len(sets)
  
    inc_idx = len(sets) -1
    solution[inc_idx] += 1
    while solution[inc_idx] > max_inc:
      solution[inc_idx] = 1
      inc_idx -= 1
      if inc_idx == 0:
        solution[0] = 0
        return solution
      solution[inc_idx] += 1
  
    for i in range(len(sets)):
      nb_workers = 0
      nb_machines = 0
      for j in range(len(sets)):
        if solution[j] == solution[i]:
          nb_workers += sets[j][0]
          nb_machines += sets[j][1]
      if nb_workers != nb_machines:
        infeasible = True
        break
  return solution

def compute_cost(sets):
  solution = [1] * len(sets)
  min_cost = compute_sol_cost(sets, solution)
  solution = get_next_sol(sets, solution)
  while solution[0] != 0:
    sol_cost = compute_sol_cost(sets, solution)
    if sol_cost < min_cost:
      min_cost = sol_cost
    solution = get_next_sol(sets, solution)
  return min_cost

input_file = open(sys.argv[1])
nb_test_cases = int(input_file.readline())

for test_case in range(nb_test_cases):
  print('Case #', test_case + 1, ': ', sep='', end='')
  n = int(input_file.readline()) 
  matrix = [''] * n
  for i in range(n):
    matrix[i] = input_file.readline()
  cost = 0
  stable = False
  while not(stable):
    stable = True
    for i in range(n):
      for j in range(n):
        disjoint = True
        for k in range(n):
          if matrix[i][k] == '1' and matrix[j][k] == '1':
            disjoint = False
            break
        if not(disjoint):
          for k in range(n):
            if matrix[i][k] == '0' and matrix[j][k] == '1':
              cost += 1
              matrix[i] = matrix[i][:k] + '1' + matrix[i][k + 1:]
              stable = False
            elif matrix[i][k] == '1' and matrix[j][k] == '0':
              cost += 1
              matrix[j] = matrix[j][:k] + '1' + matrix[j][k + 1:]
              stable = False
  matrix.sort()
  unassigned_m = [ True ] * n
  nb_empty = 0
  for i in range(n):
    for j in range(n):
      if matrix[j][i] == '1':
        unassigned_m[i] = False
        break
  sets = []
  for i in range(n):
    if unassigned_m[i]:
      sets.append([0, 1])
  
  next_i = 0
  for i in range(n):
    if i < next_i:
      continue
    nb_workers = 0
    nb_machines = 0
    for j in range(n):
     if matrix[i][j] == '1':
       nb_machines += 1
    if nb_machines == 0:
      nb_workers = 1
    else:
      next_i = n
      for k in range(i, n):
        if matrix[k] == matrix[i]:
          nb_workers += 1
        else:
          next_i = k
          break
    if nb_workers != nb_machines:
      sets.append([nb_workers, nb_machines])
  #print(sets)
  if len(sets) > 0:
    cost += compute_cost(sets)

  print(cost)
