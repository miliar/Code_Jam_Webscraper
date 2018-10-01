
# def squarefill(r,c,graph):


def fillRows(r,c,graph):
    for row in range(len(graph)):
        letter = '?'
        for col in range(len(graph[row])):
            if(graph[row][col] != '?'):
                letter = graph[row][col]
                break
        for col in range(len(graph[row])):
            if(graph[row][col] != '?' and graph[row][col] != letter):
                letter = graph[row][col]
            else:
                graph[row][col] = letter
            

def fillCols(r,c,graph):
    for col in range(len(graph[0])):
        letter = '?'
        for row in range(len(graph)):
            if(graph[row][col] != '?'):
                letter = graph[row][col]
                break
        
        for row in range(len(graph)):
            if(graph[row][col] != '?' and graph[row][col] != letter):
                letter = graph[row][col]
            else:
                graph[row][col] = letter
        
cases = int(input())
for c in range(cases):
    inp = [int(i) for i in input().split()]
    R = inp[0]
    C = inp[1]
    graph = []
    for r in range(R):
        graph.append([c for c in list(input())])
    
    # for i in range(R):
    #     for j in range(C):


    fillCols(R,C,graph)
    fillRows(R,C,graph)


    print("Case #{}:".format(c+1))
    if(len(graph) == 0):
        continue
    
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            print(graph[i][j],end='')
        print()

