fob = open("c:/inputs/codejam/B-large-practice.in",'r')
fob2 = open("c:/inputs/codejam/B-large-practice.out",'w')
numTest = int(fob.readline())
i = 0
form = "Case #%s: "
while i < numTest:
    exc = 0
    valid = 0
    input = (fob.readline()).split()
    numGooglers = int(input[0])
    excCases = int(input[1])
    maxScore = int(input[2])
    scores = input[3:]
    j=0
    while j < numGooglers:
        score = int(scores[j])
        quo = score/3
        if quo >= maxScore:
            valid = valid + 1
        else:
            if score % 3 == 0:
                if score == 0:
                    if maxScore == 0:
                        valid = valid + 1
                elif quo + 1 == maxScore:
                    if excCases > 0:
                        valid = valid + 1
                        excCases = excCases - 1
            elif score % 3 == 1:
                if quo + 1 == maxScore:
                    valid = valid + 1
            else:
                if quo + 1 == maxScore:
                    valid = valid + 1
                elif quo + 2 == maxScore:
                    if excCases > 0:
                        valid = valid + 1
                        excCases  = excCases - 1
        j = j + 1
    fob2.write(form % (str(i+1))+ str(valid)+ '\n')             
    i = i + 1
fob.close()
fob2.close()
                    
