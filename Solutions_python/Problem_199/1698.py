inp = open("i2.in","r")
out = open("o2.out","w")
cases = int(inp.readline())
for casenum in range(1,cases+1):
    minflips = 0
    case = inp.readline().split(" ")
    stack = case[0]
    size = int(case[1])
    flips = 0
    while flips < 2000:
        if "-" not in stack:
            out.write("Case #{}: {}\n".format(casenum,flips))
            break
        for pancake in range(len(stack)):
            if stack[pancake] == "-":
                if len(stack[pancake:]) < size:
                    pcake = len(stack)-size
                else:
                    pcake = pancake
                flipping = stack[pcake:pcake+size]
                new = []
                for flip in range(len(flipping)):
                    if flipping[flip] == "+":
                        new.append("-")
                    else:
                        new.append("+")
                stack = stack[0:pcake]+"".join(new)+stack[pcake+size:]
                flips += 1
                break
                
        else:
            break
    else:
        out.write("Case #{}: {}\n".format(casenum,"IMPOSSIBLE"))
    

inp.close()
out.close()
