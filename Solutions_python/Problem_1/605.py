motores = []
queries = []
def action(testActual, fileoutput):
	global motores, queries
	distance = []
	quantity_of_switches = 0
	while True :
		for m in motores:
			try:
				distance = distance + [queries.index(m)]
			except:
				distance = distance + [len(queries)]

		longest_path = max(distance)
		queries = queries[longest_path:]
		distance = []
		if len(queries) == 0:
			break
		quantity_of_switches+=1

	fileoutput.write("Case #" + str(testActual+1) + ": "+str(quantity_of_switches)+"\n")

	motores = []
	queries = []


file = open("A-small.in", "r")
fileoutput = open("output.txt", "w")
number_of_test = file.readline()
for i in range(int(number_of_test)):
	q_motores = file.readline()
	for j in range(int(q_motores)):
		motores = motores + [file.readline().lower()]

	q_queries = file.readline()
	for j in range(int(q_queries)):
		queries = queries  + [file.readline().lower()]
	action(i,fileoutput)

fileoutput.close()
file.close()



