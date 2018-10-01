import math
def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False

def is_palindrome(stringtotest):
    y = stringtotest[::-1]
    if y == stringtotest:
        return True
    else:
        return False


dataset = open("testinput.txt","r")
outfile = open("outfile.txt","w")
outputset = ""
casenumber = 1
T = int(dataset.readline())

for ammount in range(T):
    line = str(dataset.readline()).rstrip('\n').split(" ")
    A = int(line[0])
    B = int(line[1])
    Count = 0
    print(A,B)
    for number in range(A,B+1):
        if is_square(number) and is_palindrome(str(number)) and is_palindrome(str(int(math.sqrt(number)))):

            Count += 1
    print(Count)
    outputset = outputset + "Case #" + str(casenumber) +": "+str(Count)+"\n"
    casenumber += 1

print(outputset)
outfile.write(outputset)
outfile.close()
dataset.close()

