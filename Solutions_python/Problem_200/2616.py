# python2
import sys
import os.path

def process(number):
    if number=='0':
        number = '9'

def main():
    if os.path.exists('input.txt'):
        input = open('input.txt', 'r')
    else:
        input = sys.stdin
    #--------------------------------INPUT---------------------------------
    n = int(input.readline())
    results = []
    for z in xrange(n):
        init = list(map(str, input.readline().split()))
        numbers = list(init[0])
        for i, x in reversed(list(enumerate(numbers))):
            if i >0 and (int(numbers[i])<int(numbers[i-1]) or int(numbers[i]) <= 0):
                numbers[i]=9
                numbers[i-1] = int(numbers[i-1])-1
                for v in range(i,len(numbers)):
                    numbers[v] = 9
        results.append('Case #'+str(z+1)+': '+str(int(''.join(map(str,numbers)))))
    output = '\n'.join(map(str, results))
    #-------------------------------OUTPUT----------------------------------
    if os.path.exists('output.txt'):
        open('output.txt', 'w').writelines(str(output))
    else:
        sys.stdout.write(str(output))


if __name__ == "__main__":
    main()
