outF = open("2-large.out","w")

def last_tidy_number(n): # isAscensing(l):
    x = n
    while x >= 0:
        digits = [int(d) for d in str(x)]
        is_curr_number_asc = isAscensing(digits)
        if is_curr_number_asc[0]:
            return x
        else:
            i=is_curr_number_asc[1]
            digits[i]=digits[i]-1
            for q in range(i+1,len(digits)):
                digits[q]=9
            x = int(''.join(map(str,digits)))
    return 0


def isAscensing(l):
    for i, el in enumerate(l[1:]):
        # if l == [1,3,1]:
        #     print i, l[i], el, l[i] > el
        if l[i] > el:
            return (False,i)

    return (True,)

with open("B-large.in","r") as inF:
    t= int(inF.readline())
    for it in xrange(t):
        print it,	
        n = int(inF.readline().strip())
        
        answers = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:9}
        if n in answers.keys():
            res = answers[n]
        else:
            answers [n] = last_tidy_number(n)
            res = answers[n]

        print 'case #',(it+1), n, res

        outF.write("Case #%d: %d\n"%(it+1,res))

outF.close()
		
print "done"