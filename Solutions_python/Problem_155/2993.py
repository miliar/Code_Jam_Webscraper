

def count_guests_to_be_invited(s, l):
	s_max = int(s)
	total = 0
	g = 0
	for i in range(0,len(l)):
		if int(l[i]) != 0:
			if i - total <= 0:
				g = g + 0
				total = total + 0 + int(l[i])
			else:
				g = g + (i - total)
				total = total + (i-total) + int(l[i])
	
	return g

def main():
	#Read the input file
	file_handle = open("C:/Users/Dhawal/Downloads/A-large.in","r")
	file_write = open("C:/Users/Dhawal/Downloads/standing_ovation_output.txt","w")
	line_number = 0
	for line in file_handle:
		if line_number == 0:
			t = str(line).strip()
			t1 = int(t)
			line_number = line_number + 1
		else:
			#On line 2 right now
			#Split the line on space
			temp_list = str(line).split()
			guests_to_be_invited = count_guests_to_be_invited(temp_list[0].strip(), temp_list[1].strip())
			#file_write.write(line)
			file_write.write("Case #" + str(line_number) + ": " + str(guests_to_be_invited))
			if line_number >= t1:
				break 
			file_write.write("\n")
			line_number = line_number + 1
	file_handle.close()
	file_write.close()


if __name__ == "__main__":
    main()