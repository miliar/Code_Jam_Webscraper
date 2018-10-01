def generatePalindromes(currentPalindrome, current_sum):
    if len(currentPalindrome) == 0 or currentPalindrome[0] == 0:
        results = []
    else:
        results = [currentPalindrome]
    if len(currentPalindrome) > 55:
        return [] 
    for i in range(3):
        if current_sum + 2*i*i > 10:
            break
        results.extend(generatePalindromes(([i] + currentPalindrome + [i]),current_sum + 2*i*i))
    return results
    
def palindrome_generator():
    results = []
    results.extend(generatePalindromes([],0))
    results.extend(generatePalindromes([0],0))
    results.extend(generatePalindromes([1],1))
    results.extend(generatePalindromes([2],4))
    results.extend(generatePalindromes([3],9))
    results = [arrayToNumber(value) for value in results]
    results = [value * value for value in results if isPalindrome(value*value)]
    return sorted(results)
    
def getNextPalindrome(previousPalindrome):
	lowMid = (len(previousPalindrome) - 1)//2
	highMid = (len(previousPalindrome))//2
	while lowMid>=0 and highMid<len(previousPalindrome):
		if previousPalindrome[lowMid] == 9:
			previousPalindrome[lowMid]=0
			previousPalindrome[highMid]=0
			lowMid-=1
			highMid+=1
		else:
			previousPalindrome[lowMid]+=1
			if highMid != lowMid:
				previousPalindrome[highMid]+=1
			return previousPalindrome
	return [1]+[0]*(len(previousPalindrome)-1) + [1]
def arrayToNumber(array):
	sum = 0
	for digit in array:
		sum*=10
		sum+=digit
	return sum

def isSquare(number):
	sqrt = int(number**.5)
	return sqrt * sqrt == number

def squarePalindromeGen(lowerBound, upperBound):
	palindrome = [0]
	while True:
		palindrome = getNextPalindrome(palindrome)
		value = arrayToNumber(palindrome)
		if value * value > upperBound:
			return
		if value*value >= lowerBound and isPalindrome(value*value):
			yield value*value

def isPalindrome(number):

	array=[]
	while number>0:
		array.append(number%10)
		number //= 10
	for i in range(len(array)):
		if array[i] != array[len(array)-i-1]:
			return False	

	return True 
import sys
possibles = palindrome_generator()

def number_palindromes(lower,upper):
    sum = 0
    for item in possibles:
        if item >= lower and item <= upper:
            sum+=1
        if item > upper:
            break
    return sum


if __name__ == "__main__":
	lines = list(sys.stdin.readlines())		
	tests = int(lines[0].strip())
	for x,line in enumerate(lines[1:]):
		numbers = [int(value) for value in line.split()]
		lower,upper = numbers
		print("Case #"+str(x+1)+": "+str(number_palindromes(lower,upper)))
	
		
		
	
		

		


