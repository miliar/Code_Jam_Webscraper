from sys import maxint

def train_times(turnaround, AB,BA):
    AB.sort()
    BA.sort()
    A_start = 0
    B_start = 0
    at_A = 0
    at_B = 0
    time = 0
    A_moving_B = []
    B_moving_A = []
    while len(AB) > 0 and len(BA) > 0:
        nextAB = AB[0]
        nextBA = BA[0]
        next = min(nextAB,nextBA)
        time = next[0]
        for i in range(0,len(A_moving_B)):
            if A_moving_B[i][1] + turnaround <= time:
                at_B += 1
                A_moving_B[i] = (-1,maxint)
        for i in range(0,len(B_moving_A)):
            if B_moving_A[i][1] + turnaround <= time:
                at_A += 1
                B_moving_A[i] = (-1,maxint)
        clean(A_moving_B)
        clean(B_moving_A)
        if nextBA < nextAB:
            B_moving_A.append(nextBA)
            BA[0:1] = []
            if at_B == 0:
                B_start += 1
            else:
                at_B -= 1
        else:
            A_moving_B.append(nextAB)
            AB[0:1] = []
            if at_A == 0:
                A_start += 1
            else:
                at_A -= 1

    while len(AB) > 0:
        next = AB[0]
        time = next[0]
        for i in range(0,len(A_moving_B)):
            if A_moving_B[i][1] + turnaround <= time:
                at_B += 1
                A_moving_B[i] = (-1,maxint)
        for i in range(0,len(B_moving_A)):
            if B_moving_A[i][1] + turnaround <= time:
                at_A += 1
                B_moving_A[i] = (-1,maxint)
        A_moving_B.append(next)
        clean(A_moving_B)
        clean(B_moving_A)
        AB[0:1] = []
        if at_A == 0:
            A_start += 1
        else:
            at_A -= 1

    while len(BA) > 0:
        next = BA[0]
        time = next[0]
        for i in range(0,len(A_moving_B)):
            if A_moving_B[i][1] + turnaround <= time:
                at_B += 1
                A_moving_B[i] = (-1,maxint)
        for i in range(0,len(B_moving_A)):
            if B_moving_A[i][1] + turnaround <= time:
                at_A += 1
                B_moving_A[i] = (-1,maxint)
        B_moving_A.append(next)
        clean(A_moving_B)
        clean(B_moving_A)
        BA[0:1] = []
        if at_B == 0:
            B_start += 1
        else:
            at_B -= 1
    return (A_start,B_start)

def clean(times):
    try:
        times.remove((-1,maxint))
        clean(times)
    except:
        pass
       
        
n = int(raw_input())
for i in range(1,n+1):
    turn = int(raw_input())
    temp = raw_input()
    temp = temp.split(' ')
    a = int(temp[0])
    b = int(temp[1])
    AB = []
    BA = []
    for j in range(0,a):
        temp = raw_input()
        temp = temp.split(' ')
        start = temp[0].split(':')
        start_time = int(start[0]) * 60 + int(start[1])
        end = temp[1].split(':')
        end_time = int(end[0]) * 60 + int(end[1])
        AB.append((start_time,end_time))
    for j in range(0,b):
        temp = raw_input()
        temp = temp.split(' ')
        start = temp[0].split(':')
        start_time = int(start[0]) * 60 + int(start[1])
        end = temp[1].split(':')
        end_time = int(end[0]) * 60 + int(end[1])
        BA.append((start_time,end_time))
    answer = train_times(turn,AB,BA)
    print "Case #%d: %d %d" % (i, answer[0], answer[1])
