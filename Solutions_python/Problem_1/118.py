DEBUG = 1

def log(msg):
  if DEBUG:
    print msg

for caseno in range(int(raw_input())):
  stations = []
  for ignore in range(int(raw_input())):
    stations.append(raw_input())
  solutions = {}
  for station in stations:
    solutions[station] = 0
  
  for ignore in range(int(raw_input())):
    new_station = raw_input()
    for solution_last_station in solutions.keys():
      if new_station == solution_last_station:
        switches = solutions[new_station] + 1
        solutions.pop(new_station)
        for station in stations:
          if station != solution_last_station and solutions.get(station, 1001) > switches:
            solutions[station] = switches
  fastest_solution = min(solutions.values())
  print "Case #%s: %s" % (str(caseno + 1), str(fastest_solution))