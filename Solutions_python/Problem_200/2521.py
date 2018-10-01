# coding: utf-8

def main():
	T = int(raw_input())
	
	for ka in range(T):
		bf = raw_input()
		n = int(bf)
		ans = 0
		for i in bf:
			ans = ans*10 + 1
		if ans > n:
			ans = ans / 10
		
		anslen = len(str(ans))
		
		for i in range(anslen):
			tmp = 0
			for j in range(anslen-i):
				tmp = tmp*10 + 1
			# print 'tmp = ', tmp
			while ans + tmp <= n and ans%10 < 9:
				ans = ans + tmp
		print 'Case #{}: {}'.format(ka+1, ans)

if __name__ == '__main__':
	main()