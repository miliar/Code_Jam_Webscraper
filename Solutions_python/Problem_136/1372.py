from sys import stdin

Q = int(stdin.readline())
for qq in xrange(Q):
  farm_cost, farm_prod, target = map(float, stdin.readline().split())
  prod = 2.0
  so_far_time = 0.0
  finish_time = target/prod
  prospective_finish_time = farm_cost / prod + target / (prod+farm_prod)
  while prospective_finish_time < finish_time:
    so_far_time += farm_cost / prod
    prod += farm_prod
    finish_time = target/prod
    prospective_finish_time = farm_cost / prod + target / (prod+farm_prod)
  print("Case #"+str(qq+1)+": "+str(so_far_time + target/prod))