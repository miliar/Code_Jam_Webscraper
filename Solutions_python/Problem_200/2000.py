import sys
def numToRight(num,x):
    return num%pow(10,x)

def isTidy(num):
    tidy = True
    numstring = str(num)
    for count in range(0,len(numstring)-1):  
        if int(numstring[count]) > int(numstring[count+1]):
            tidy=False
    return tidy

def tidier(num):
	for place in range(1,len(str(num))):
	    con= numToRight(num,place+1)
	    if not(isTidy(con)):
	        num = num - numToRight(num,place) - 1
	return str(num)

def read_in():
	tests = sys.stdin.readline()
	counts = int(tests.rstrip())
	for each in range(1,counts + 1):
		line = sys.stdin.readline()
		print('Case #' + str(each) + ':', tidier(int(line.rstrip())))
def main():
	lines = read_in()
if __name__ == '__main__':
	main()