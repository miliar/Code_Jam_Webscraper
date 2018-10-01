f = open('A-large.in', 'r+')
o = open('output_large.out', 'w+')
cases = int(f.readline())
case_num = 1

while(cases != 0):
    line = f.readline().split()
    snappers = int(line[0])
    finger_snaps = int(line[1])

    divisor = 2**snappers
    cociente = finger_snaps / divisor
    residuo = finger_snaps % divisor

    if (residuo  == divisor - 1):
        result = "ON"
    else:
        result = "OFF"

    o.write("Case #" + str(case_num) + ": " + result + "\n")
    #print "Ganancia: " + str(ganancia)
    
    cases -= 1
    case_num += 1

f.close()    
o.close()
