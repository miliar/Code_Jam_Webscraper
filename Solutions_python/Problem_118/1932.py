# open output file
fout = open('outputQ3.txt', 'w+')
	
# open input file	
fin = open('C-small-attempt0.in', 'r')
fin.seek(0)

file_line = fin.readline()

n = file_line
print 'number of casees: ' + n

def is_palindrome(arr):
        arr = str(arr)
        return arr == arr[::-1]

def is_square(posint):
        if posint == 1:
                return True
        x = posint // 2
        seen = set([x])
        while x * x != posint:
                x = (x + (posint // x)) // 2
                if x in seen: return False
                seen.add(x)
        return True

def isqrt(x):
        n = int(x)
        if n == 0:
                return 0
        a, b = divmod(n.bit_length(), 2)
        x = 2**(a+b)
        while True:
                y = (x + n//x)//2
                if y >= x:
                        return x
                x = y


for case in range(int(n)):

        line1 = fin.readline()
        low_bound = int(line1.split(' ')[0])
        up_bound = int(line1.split(' ')[1])

        count = 0
        
        for i in range(low_bound,up_bound+1):
                if is_palindrome(i):
                        if is_square(i):
                                if is_palindrome(isqrt(i)):
                                        count = count + 1
                                                        
        fout.write('Case #' + str(case+1) + ': ' + str(count) + '\n')

fout.flush()

fout.close()
