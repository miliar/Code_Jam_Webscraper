from sys import stdin,stdout

def istidy(number):
    splitted = list(str(number))
    for i in range(len(splitted)-1):
        if(not(int(splitted[i]) <= int(splitted[i+1]))):

            return False

    return True

def tidynumber(input):
    input = int(input)
    for counter in range(input,0,-1):
        if(istidy(counter)):
            return counter

if __name__ == '__main__':
    n = (stdin.readline())
    n= int(n)
    for i in range(n):
        stdout.write("Case #"+str(i+1)+": "+str(tidynumber(stdin.readline()))+ '\n')


