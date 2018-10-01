test_cases = int(raw_input())

class Task():
   def __init__(self, agent, button_location):
      self.agent  = agent
      self.button_location = button_location
   
   def __repr__(self):
      return 'Task(%s, %s)' % (repr(self.agent), repr(self.button_location))
      
class TestCase():
   def __init__(self, i, line = None, tasks = None):
      self.id = i
      
      if line:
          line = line.split(" ")
          self.number_of_tasks = int(line[0])
          self.tasks = []
          
          for i in range(self.number_of_tasks):
             task = Task(line[2*i+1], int(line[2*i+2]))
             self.tasks.append(task)
      elif tasks:
         self.number_of_tasks = len(tasks)
         self.tasks = tasks     
   
   def __repr__(self):
      return 'TestCase(%s, tasks = %s)' % (self.id, repr(self.tasks))
   
   def __str__(self):
      return 'Case #%s: ' % self.id

class Solver():
       
    def solve(self, test_case):
       agent_locations = { 'O' : 1, 'B' : 1 }
       time_saved    = 0
       time_elapsed  = 0
       previous_task = None
       for task in test_case.tasks:
           agent = task.agent
           time_to_execute = abs(agent_locations[agent] - task.button_location) + 1
           
           if previous_task and previous_task.agent == task.agent:
               time_saved   += time_to_execute
               time_elapsed += time_to_execute
           else:
               time_to_execute_without_pushing = time_to_execute - 1
               
               time_to_execute_without_pushing = max(time_to_execute_without_pushing-time_saved, 0)
               
               time_to_execute = time_to_execute_without_pushing + 1 
               
               time_elapsed += time_to_execute
               time_saved = time_to_execute
          
           previous_task = task
           agent_locations[agent] = task.button_location
         
       return time_elapsed
       
solver = Solver()

for case_i in range(test_cases):
    
    line = raw_input()
    
    test_case = TestCase(case_i + 1, line = line)
    
    print '%s%s' % (test_case, solver.solve(test_case))


