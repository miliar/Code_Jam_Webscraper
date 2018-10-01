import Queue

inputfile = open("C-small.in", "r")
lines = ""

cases = int(inputfile.readline().strip())

for i in range(0, cases):
    total = 0
    q = []
    tempList = inputfile.readline().strip().split()
    R = int(tempList[0])
    k = int(tempList[1])
    N = int(tempList[2])
    queuelist = inputfile.readline().strip().split()
    for item in queuelist:
        q.append(int(item))
    waiter = 0
    for element in range(0, R):
        people = 0
        new_queue = []
        while len(q) > 0 and people + q[0] <= k:
            people += q[0]
            total += q[0]
            new_queue.append(q.pop(0))
        for w in new_queue:
            q.append(w)
            

    
    lines += "Case #%d: " %(i + 1) + str(total) + "\n"
outputfile = open("C-small.out", "w")
outputfile.writelines(lines)
outputfile.close()
inputfile.close()


    
            