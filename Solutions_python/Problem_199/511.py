import sys

def main():
	T = int(input())

	for t in range(1, T+1):
		s,k = input().split()
		k = int(k)
		ans = 0
		s = list(s)

		for i in range(0, len(s)-k+1):
			if str(s[i]) == '-':
				ans+=1
				for j in range(i,i+k):
					if str(s[j]) == '+':
						s[j] = '-'
					else:
						s[j] = '+'
			# print(s)

		flag = 0
		for i in s:
			if str(i) == '-':
				flag = 1
				break

		print ("Case #" + str(t) + ": ", end="")
		if flag:
			print ("IMPOSSIBLE")
		else:
			print (str(ans))


if __name__ == "__main__":
	main()