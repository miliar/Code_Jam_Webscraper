import math
import sys
known_palindromes = set()
def is_palindrome(number):
    global max_palindrome
    a = str(number)
    if number in known_palindromes:
        return True
    for n in range(len(a)//2):
        if a[n] != a[-1-n]:
            return False
    known_palindromes.add(number)
    return True 

def main():
    with open(sys.argv[1]) as input:
        with open(sys.argv[2],'w') as out:
            cases = int(input.readline().strip())
            for case in range(1,cases+1):
                output = 0
                start, end = [int(a) for a in input.readline().split()]
                for i in range(int(math.sqrt(start)),int(math.sqrt(end))+1):
                    if is_palindrome(i) and i*i>=start and is_palindrome(i**2):
                        output +=1
                txt = 'Case #{}: {}\n'.format(case,output)
                print(txt)
                out.write(txt)



if __name__=='__main__':
    main()
