# -*- coding: utf-8 -*-

inp = open("A-large.in","r")
outp = open("output.out","w")

lines = inp.readline()
lines = lines.split()
lines = int(lines[0])

for i in range (0,lines):
    outp.write ("Case #" + str(i+1) + ": ")
    test = inp.readline()
    test = test.split ()
    test = int(test[0])
    wires = []
    intersections = 0

    for a in range (0,test):
        wire = inp.readline()
        wire = wire.split ()
        wire1 = int(wire[0])
        wire2 = int(wire[1])
        wir = []
        wir.append(wire1)
        wir.append(wire2)
        for w in wires:
            if wire1 < w[0] and wire2 > w[1]:
                intersections += 1
            elif wire1 > w[0] and wire2 < w[1]:
                intersections += 1
        wires.append(wir)
    
    outp.write (str(intersections) + '\n')


inp.close()
outp.close()

