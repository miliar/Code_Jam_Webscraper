#!/usr/bin/env python
import sys
import datetime

num_cases = -1

fileIN = open(sys.argv[1], "r")

num_cases = int(fileIN.readline())

for case_num in range(num_cases):    
    trains_a = []
    trains_b = []
    depart_a = []
    depart_b = []
    misses_a = 0
    misses_b = 0
    
    turnaround = int(fileIN.readline())
    line = str(fileIN.readline()).strip()
    parts = line.split(' ')

    num_a = int(parts[0])
    num_b = int(parts[1])
    
    #
    #   Load times from file
    #
    for i in range(num_a):
        line = str(fileIN.readline()).strip()
        parts = line.split(' ')
        
        time_1 = str(parts[0]).split(':')
        time_2 = str(parts[1]).split(':')
        depart_a.append((datetime.time(int(time_1[0]), int(time_1[1])),
                         datetime.time(int(time_2[0]), int(time_2[1]))))


    for i in range(num_b):
        line = str(fileIN.readline()).strip()
        parts = line.split(' ')

        time_1 = str(parts[0]).split(':')
        time_2 = str(parts[1]).split(':')
        depart_b.append((datetime.time(int(time_1[0]), int(time_1[1])),
                         datetime.time(int(time_2[0]), int(time_2[1]))))
    
    depart_a.sort()
    depart_b.sort()
    #
    #   Process lists
    #
    while depart_a or depart_b:
        #   All going one way -> depts - waiting trains
        if depart_a and not depart_b:
            while depart_a:
                departing = depart_a.pop(0)
                if trains_a and trains_a[0] <= departing[0]:
                    trains_a.pop(0)
                else:
                    misses_a += 1

        if depart_b and not depart_a:
            while depart_b:
                departing = depart_b.pop(0)
                if trains_b and trains_b[0] <= departing[0]:
                    trains_b.pop(0)
                else:
                    misses_b += 1
        
        #   Normal trip A to B
        if depart_a and depart_b and depart_a[0][0] < depart_b[0][0]:
            if not trains_a or trains_a[0] > depart_a[0][0]:
                misses_a += 1
            else:
                trains_a.pop(0)
                        
            dept_time = depart_a[0][0]
            arrv_time = depart_a[0][1]
            
            add_hours = (turnaround + depart_a[0][1].minute) / 60
            new_hours = depart_a[0][1].hour + add_hours
            new_mins = (turnaround + depart_a[0][1].minute) % 60
            new_time = datetime.time(new_hours, new_mins)
            
            depart_a.pop(0)            
            trains_b.append(new_time)
            trains_b.sort()
        
        #   Normal trip B to A   
        if depart_a and depart_b and depart_b[0][0] < depart_a[0][0]:
            if not trains_b or trains_b[0] > depart_b[0][0]:
                misses_b += 1
            else:
                trains_b.pop(0)
                        
            dept_time = depart_b[0][0]
            arrv_time = depart_b[0][1]
            
            add_hours = (turnaround + depart_b[0][1].minute) / 60
            new_hours = depart_b[0][1].hour + add_hours
            new_mins = (turnaround + depart_b[0][1].minute) % 60
            new_time = datetime.time(new_hours, new_mins)
            
            depart_b.pop(0)            
            trains_a.append(new_time)
            trains_a.sort()

        #   Simultaneous A and B
        if depart_a and depart_b and depart_a[0][0] == depart_b[0][0]:
            if not trains_a or trains_a[0] > depart_a[0][0]:
                misses_a += 1
            else:
                trains_a.pop(0)

            dept_time = depart_a[0][0]
            arrv_time = depart_a[0][1]
            
            add_hours = (turnaround + depart_a[0][1].minute) / 60
            new_hours = depart_a[0][1].hour + add_hours
            new_mins = (turnaround + depart_a[0][1].minute) % 60
            new_time = datetime.time(new_hours, new_mins)
            
            depart_a.pop(0)            
            trains_b.append(new_time)
            trains_b.sort()
            dept_time = depart_b[0][0]
            arrv_time = depart_b[0][1]

            if not trains_b or trains_b[0] > depart_b[0][0]:
                misses_b += 1
            else:
                trains_b.pop(0)
                
            add_hours = (turnaround + depart_b[0][1].minute) / 60
            new_hours = depart_b[0][1].hour + add_hours
            new_mins = (turnaround + depart_b[0][1].minute) % 60
            new_time = datetime.time(new_hours, new_mins)
            
            depart_b.pop(0)            
            trains_a.append(new_time)
            trains_a.sort()            
        
    sys.stdout.write("Case #" + str(case_num+1) + ": " +
                     str(misses_a) + " " + str(misses_b) + "\n")
    
