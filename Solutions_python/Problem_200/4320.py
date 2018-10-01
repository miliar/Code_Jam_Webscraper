output = ""
with open("code_jam_17_02_test.txt") as f:
	N = f.next()
	line_num=1
	for line in f:
		line = line.strip()
		tidy_number = int(line)
		if tidy_number<10:
			output+= 'CASE #'+str(line_num)+': '+str(tidy_number) +'\n'
		else:
			S = map(str,line)[::-1]
			for i,C in enumerate(S):
				if i< (len(S)-1):
					if int(C)<int(S[i+1]):
						S[0:(i+1)] = [str(9)] * len(S[0:(i+1)])
						S[i+1] = str(int(S[i+1])-1)
			S = ''.join(S[::-1])
			tidy_number = int(S)
			output+= 'CASE #'+str(line_num)+': '+str(tidy_number) +'\n'
		line_num+=1
	f.close()

output = output.strip()
print output

with open("code_jam_test_output.txt","w") as r:
	r.write(output)
	r.close()