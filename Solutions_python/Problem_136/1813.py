open('output.in','w').close()

with open('input.in') as file:
    lines = file.readlines()
    line = 0
    T = int(lines[line])
    line += 1
    for i in range(T):
        ratio = 2.0
        time = 0.0
        C = float(lines[line].split()[0])
        F = float(lines[line].split()[1])
        X = float(lines[line].split()[2])
        time_to_end = X/ratio
        time_to_farm = C/ratio
        while not time_to_end < time_to_farm+(X/(ratio+F)):
            time += time_to_farm
            ratio += F
            time_to_end = X/ratio
            time_to_farm = C/ratio
        time += time_to_end
        line += 1
        with open('output.in','rw+') as file:
            file.seek(0, 2)
            file.write('Case #'+str(i+1)+': '+str(time)+'\n')
