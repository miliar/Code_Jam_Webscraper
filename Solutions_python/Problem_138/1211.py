input_file = open('D-large.in', 'r')
out = open('war_output.txt', 'w')
num_testcases = input_file.readline()
num_testcases = int(num_testcases)
print num_testcases
for idx in range(0, num_testcases):
  n = int(input_file.readline())
  naomi = input_file.readline().split()
  ken = input_file.readline().split()
  naomi = map(float, naomi)
  ken = map(float, ken)
  naomi = sorted(naomi)
  ken = sorted(ken)
  start_naomi = naomi[:]
  start_ken = ken[:]
  optimal_war = 0
  for round in range(0, n):
    c_n = max(naomi)
    valid = []
    for opt_ken in ken:
      if opt_ken > c_n:
        valid.append(opt_ken)
    c_k = min(ken)
    if len(valid) is not 0:
      c_k = min(valid)
    if c_n > c_k:
      optimal_war += 1
    ken.remove(c_k)
    naomi.remove(c_n)
  optimal_deciet = 0;
  naomi = start_naomi
  ken = start_ken
  for round in range(0, n):
    c_n = max(naomi)
    beats = []
    for opt_ken in ken:
      if c_n > opt_ken:
        beats.append(opt_ken)
    if (len(beats) > 0):
      force_ken = max(beats)
      tell_ken = force_ken - .0000000001
    else:
      tell_ken = c_n
    valid = []
    for opt_ken in ken:
      if opt_ken > tell_ken:
        valid.append(opt_ken)
    c_k = min(ken)
    if len(valid) is not 0:
      c_k = min(valid)
    if c_n > c_k:
      optimal_deciet += 1
    ken.remove(c_k)
    naomi.remove(c_n)

  ans = str(optimal_deciet) + " " + str(optimal_war)
  out.write("Case #" + str(idx+1) + ": " + str(ans) + '\n');

