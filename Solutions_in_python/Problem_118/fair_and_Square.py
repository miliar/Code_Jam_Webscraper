from math import sqrt

fr = open('input.in' , 'r')
fw = open('output.out', 'w')

nr_cases = 0

i = 0

for line in fr:
	

	if nr_cases == 0 :
		nr_cases = line

	else:
		i=i+1

		n , m = line.split(" ")
		
		n=int(n)
		m=int(m)

		contatore = 0

		for nr in xrange(n,m+1):
			stringa = str(nr)
			radice_nr = sqrt(nr)

			str_temp = str(radice_nr)
			if(str_temp[-1] == '0' and str_temp[-2] == '.'):
				

				str_temp = str(int(radice_nr))
				# print str_temp

				simmetrica  =  stringa[::-1]
				simmetrica_radice = str_temp[::-1]

				print str(nr) +"     "+simmetrica
				print str_temp + "   " + simmetrica_radice


				if simmetrica == str(nr) and simmetrica_radice == str_temp:
					contatore +=1

		fw.write("Case #" + str(i) + ": " + str(contatore) + "\n")

		

fr.close()
fw.close()