import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def CalculatePlace(stallset):
    calculated = []
    for s in range(len(stallset)):
        if stallset[s] == 1:
            continue
        else:
            left = 0
            for x in stallset[s-1:0:-1]:
                if x == 1:
                    break
                left += 1
            right = 0
            for x in stallset[s+1:]:
                if x == 1:
                    break
                right += 1
        calculated.append((s,left,right))
    initial = (0,0,0)
    for calc,left,right in calculated:
        if min(left,right) > min(initial[1],initial[2]):
            initial = (calc,left,right)
        elif min(left,right) < min(initial[1],initial[2]):
            continue
        elif max(left,right) > max(initial[1],initial[2]):
            initial = (calc,left,right)
        elif max(left,right) < max(initial[1],initial[2]):
            continue
        elif initial[0]>calc:
            initial = (calc,left,right)
    stalls[initial[0]] = 1
    return (initial[1],initial[2])
    
            

inp = open("is1.in","r")
out = open("os1.out","w")
cases = int(inp.readline())
for casenum in range(1,cases+1):
    inputs = inp.readline().split(" ")
    stallno = inputs[0]
    stalls = [1]
    stalls += [0]*int(stallno)
    stalls += [1]
    for n in range(int(inputs[1])):
        left,right = CalculatePlace(stalls)
    out.write("Case #{}: {} {}\n".format(casenum,max(left,right),min(left,right)))
    

inp.close()
out.close()
