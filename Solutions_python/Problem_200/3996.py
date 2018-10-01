




def is_tidy(number_string):
	max_digit = 0
	for ch in number_string:
		if(int(ch) < max_digit):
			return False
		if(int(ch) >= max_digit):
			max_digit = int(ch)
	return True


def naive_solver(num):

	cur_num = num
	while(not is_tidy(cur_num)):
		cur_num -= 1
	return cur_num

def smart_solver(str_num):
	#saved_num = num
	nstr = list(str_num)
	str_size = len(nstr)

	max_size = 0

	for i in range(0, str_size-1):

		#see if the next character is larger than the current one
		while(int(nstr[i]) > int(nstr[i+1])):

			#if it's larger,decrease the current number by -1 and add 9 to the up coming digits
			new_val = int(nstr[i]) -1


			if(new_val >= 0):
				nstr[i] = str(new_val)
				#all following are 9s
				for f in range(i+1,str_size):
					nstr[f] = "9"
				return "".join(nstr)
			
			#this means we need to borrow one from the front
			if(new_val == -1):
				loop_index = i-1
				#makesure 
				while( loop_index >= 0 and nstr[loop_index] != -1):
					nstr[loop_index] = int(nstr[loop_index]) - 1
					if(nstr[loop_index] != -1):
						break
					loop_index -=1

				#special end case
				if(loop_index == 0 and nstr[loop_index] == -1):
					answer = []
					for x in range(1,str_size):
						answer.push(9)
					return "".join(answer)

				nstr[i] = str(new_val)
				for x in range(i+1, str_size):
					nstr[x] = "9"

				return "".join(nstr)


			#increase index
			i += 1

	return "".join(nstr)



# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for t_num in range(1, t + 1):
  n = str(input())  # read a list of integers, 2 in this case
  str_num = n


  answer = str_num
  while(not is_tidy(answer)):
  	answer = smart_solver(answer)


  #drop leading zeros
  stopper = 0
  for i,x in enumerate(answer):
  	if(x != '0'):
  		break
  	else:
  		stopper += 1

  	answer = answer[stopper:]
  	if(answer == ""):
  		answer = "0"


  print("Case #{}: {}".format(t_num,answer))
  # check out .format's specification for more formatting options


  # 1900 
  # - 1



  # 1000 -> 999
  # 1200 -> 1119