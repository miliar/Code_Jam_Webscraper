def recursive_dfs(graph, start, path=[]):
  '''recursive depth first search from start'''
  path=path+[start]
  for node in graph[start]:
    if not node in path:
      path=recursive_dfs(graph, node, path)
  return path

def iterative_dfs(graph, start, path=[]):
  '''iterative depth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if v not in path:
      path=path+[v]
      q=graph[v]+q
  return path

def iterative_bfs(graph, start, path=[]):
  '''iterative breadth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if not v in path:
      path=path+[v]
      q=q+graph[v]
  return path

'''
   +---- A
   |   /   \
   |  B--D--C
   |   \ | /
   +---- E
'''
#{'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
graph = {1:[2,7,8],2:[1,3,6],3:[2,4,5],4:[3],5:[3],6:[2],7:[1],8:[9,12],9:[10,11],10:[9],11:[9],12:[8]}
print 'recursive dfs ', recursive_dfs(graph, 1)
print 'iterative dfs ', iterative_dfs(graph, 1)
print 'iterative bfs ', iterative_bfs(graph, 1)

a = [6]
b = [3]
print a.append(b[0])
