from math import ceil, floor



def calculate(hist,nmin, nmax, p, remS, N, offset):
    possible_answers = False
   # if (remS < 0 or ((nmin + offset) * N < remS)):
       # return False
    if (remS < 0 or nmin < 0):
        return False
    if (N == 0):
        return remS == 0

    avg = float(remS)/N

    fl = floor(avg)
    cl = ceil(avg)
    possibleInterval = [i for i in [cl + 1, cl, fl, fl - 1] if (nmax - offset <= i and nmin + offset >= i)]
    if (N == 1):
        ans = remS in possibleInterval
        nmax = max(nmax, remS)
       # if (ans and (nmax >= p)):
         #   print(hist +"|" +  str(remS))
          #  if (offset == 1):
         #       print("normal")
        #    else:
       #         print("surprising.")
        return (ans and (nmax >= p))
    for ps in possibleInterval:
        
        newmax = max(ps, nmax)
        newmin = min(ps, nmin)
        newRemS = remS - ps
        newN = N - 1
        newHist = hist + "|" + str(ps)
        possible_answers = possible_answers or  calculate(newHist, newmin, newmax, p, newRemS, newN, offset)

    return possible_answers









def normal(score, N, p):
    N = 3
    if (score == 0):
        return p == 0
    offset = 1
    avg = float(score) / 3
    fl = floor(avg)
    cl = ceil(avg)
    return calculate("",fl,fl,p,score,N,offset) or calculate("",cl,cl,p,score,N,offset)
    

def surprising(score, N, p):
    N = 3
    if (score == 0):
       return p == 0
    offset = 2
    avg = float(score) / 3
    fl = floor(avg)
    cl = ceil(avg)
    return  calculate("",fl,fl,p,score,N,offset)



def main():
    lines = []
    f = open('data.txt',"r")
    for i in f:
        lines.append(i)
    n = int(lines[0])
    for ln in range(1,len(lines)):
        t = lines[ln].split(" ")
        N = int(t[0]) #the number of googlers
        S = int(t[1]) #number of surprising triplets
        p = int(t[2]) #best result of that
        scores = [int(i) for i in t[3:]]
        
        non = 0 #number of googlers that have a p normally
        nos = 0 #number of surprising. not included in normals.
       
        for score in scores:
            isnormal = normal(score, N, p)
            if (isnormal):
                non = non + 1
            else:
                issurp =  surprising(score, N, p)
                if (issurp):
                    nos = nos + 1

      #  print("Normal: " + str(non) + " surprising: " + str(nos) + " allowed: " + str(S))
        res = non + (min(nos, S))


        print("Case #" + str(ln) + ": " + str(res))



if __name__ == "__main__":
    main()
