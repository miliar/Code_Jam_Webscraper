f = open('C-small-attempt0.in', 'r+')
o = open('Result.out', 'w+')
cases = int(f.readline())
case_num = 1

while(cases != 0):
    config = f.readline().split()
    viajes = int(config[0])
    pasajeros = int(config[1])
    grupos = f.readline().split()    
    grupos = map(int,grupos)
    ganancia = 0

    while (viajes > 0):
        cuenta = 0
        cola = []

        while (len(grupos) and ((cuenta + grupos[0]) <= pasajeros)):            
            current = grupos[0]
            cola += [grupos[0]]
            cuenta += current
            ganancia += current            
            grupos = grupos[1:]

        grupos += cola
        viajes -= 1

    o.write("Case #" + str(case_num) + ": " + str(ganancia) + "\n")
    print "Ganancia: " + str(ganancia)
    
    cases -= 1
    case_num += 1

f.close()    
o.close()
