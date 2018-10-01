import sys
import copy

f = open(sys.argv[1], "r")
lines = f.readlines()
f.close()

cases = int(lines[0])
case_no = 0

index = 1
while(case_no != cases):
    case_no += 1
    index += 1

    a1 = sorted(map(lambda x: float(x), lines[index].split(" ")), reverse=True)
    index += 1
    a2 = sorted(map(lambda x: float(x), lines[index].split(" ")), reverse=True)
    index += 1


    # If she is playing faithfully.
    no_fault = 0
    temp = 0

    a1c = copy.deepcopy(a1)
    a2c = copy.deepcopy(a2)
    l = 0
    while (l != len(a1)):
        l += 1
        if a1c[0] > a2c[0]:
            no_fault += 1
            a1c = a1c[1:]
            a2c = a2c[:-1]
        else:
            ii = 1
            while(ii < len(a2c) and a2c[ii] > a1c[ii]):
                ii += 1
            a2c.remove(a2c[ii -1])
            a1c = a1c[1:]
            

    # If she is being a deceit.
    fault = 0
    
    # Except the ones which are smaller than the smallest of a2, 
    # all should give her points.
    l = 0
    ll = len(a1)
    while(l < ll):
        l += 1
        #print "Before", a1, a2, fault
        if (a1[-1] < a2[-1]):
            a1 = a1[:-1]
            a2 = a2[1:]
        else:
            a1 = a1[:-1]
            a2 = a2[:-1]
            fault += 1
        #print "After", a1, a2, fault

    print "Case #" + str(case_no) + ": " + str(fault) + " " + str(no_fault)


