def main():
	t = int(input())
	for i in range(1, t+1):
		number = int(input())
		#print("Checking",number)
		lastTidy = findLastTidy(number)
		print("Case #"+str(i)+":",lastTidy)

		
		
def findLastTidy(number):
	for num in range(number, 0, -1):
		#print("--Checking",num)
		if(isTidy(num)):
			return num
		#print("--",num,"is not tidy")
			
def isTidy(num):
	if(num == (num%10)):
		return True
	lastDigit = num % 10
	num = int(num / 10)
	secondLastDigit = num % 10
	if(lastDigit >= secondLastDigit):
		return isTidy(num)
	else:
		return False
	

















main()