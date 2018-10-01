
def solve(cipher): 
    inputs = cipher.split(" ") 
    X = int(inputs[0])
    R = int(inputs[1])
    C = int(inputs[2])

    total = R*C
    #print total, X
    if total%X!=0:
        return "RICHARD"

    if X==1:
        return "GABRIEL"

    if X==2:
        return "GABRIEL"

    if X==3:
        if total==3:
            return "RICHARD"
        return "GABRIEL"
    if X==4:
        if total==4 or total==8:
            return "RICHARD"
        return "GABRIEL"
    return "GABRIEL"

if __name__ == "__main__": 
    testcases = input() 
    for caseNr in xrange(1, testcases+1): 
        cipher = raw_input() 
        print("Case #%i: %s" % (caseNr, solve(cipher)))