
import math

def palindrome(num):
    for i in range(int(len(num)/2)):
        if num[i] != num[len(num)-i-1]:
            return False

    return True

if __name__ == "__main__":

    finput = open("/home/alexandre/codejam/FairAndSquare/C-small-attempt0.in", 'r')
    foutput = open("/home/alexandre/codejam/FairAndSquare/C-small-attempt0.out", 'w')

    num_cases = int(finput.readline())

    for case in range(num_cases):
        [A, B] = [int(X) for X in finput.readline().split()]

        tuples = [(str(x), str(x*x)) for x in range(int(math.ceil(math.sqrt(A))), int(math.sqrt(B))+1)]
        hits = [(x,y) for (x,y) in tuples if palindrome(x) and palindrome(y)]

        foutput.write("Case #"+str(case+1)+": "+str(len(hits))+"\n")

    finput.close()
    foutput.close()

