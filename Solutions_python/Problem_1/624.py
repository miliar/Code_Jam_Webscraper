#!/usr/bin/python
#-*- coding=utf-8

def analize_case(engines_list, queries_list):
	switches=0
	#The easiest case
	for engine in engines_list:
		if engine not in queries_list:
			return switches
			
	#The hard way
	positions=map_engines(engines_list, queries_list)
	switches=analize_positions(positions)
	return switches
	
def map_engines(engines_list, queries_list):
	#Mapping the locations of enignes in queries_list
	positions={}
	for engine in engines_list:
		positions[engine]=[]
		for i in range(len(queries_list)):
			if engine==queries_list[i]:
				positions[engine].append(i)
				
	return positions

def analize_positions(positions, actual_engine="", switches=0, bigger_step=0):
	#The base case
	for engine in positions.keys():
		if len(positions[engine])==0:
			return switches
			
	#The main algorithm
	for engine in positions.keys():
		if positions[engine][0]>bigger_step:
			if engine != actual_engine:
				bigger_step=positions[engine][0]
				actual_engine=engine
	switches+=1
			
	#Now, cleaning positions
	for engine in positions.keys():
		static_len=len(positions[engine])
		for i in range(static_len):
			if positions[engine][0]<bigger_step:
				del positions[engine][0]
				
	#Everything again 	
	return analize_positions(positions, actual_engine, switches, bigger_step)
	
################################################################################

def read_input(input_file):
	input_file=open(input_file)
	input=input_file.readlines()
	cases=[]
	cases_number=int(input[0])
	trash=input.pop(0)
	for i in range(cases_number):
		engines_number=int(input[0])
		trash=input.pop(0)
		engines_list=[]
		for i in range(engines_number):
			engines_list.append(input[0].lower())
			trash=input.pop(0)
			
		queries_number=int(input[0])
		trash=input.pop(0)
		queries_list=[]
		for i in range(queries_number):
			queries_list.append(input[0].lower())
			trash=input.pop(0)
		cases.append((engines_list, queries_list))
	return cases
	
def write_output(output_file, case, switches):
	output_file=open(output_file, 'a')
	output="Case #%i: %i\n" %(case, switches)
	output_file.write(output)
	output_file.close()
	

if __name__=="__main__":
	import sys
	input_file=sys.argv[1]
	output_file=sys.argv[2]

	cases=read_input(input_file)
	print_number_case=0
	for i in range(len(cases)):
		print_number_case+=1
		switches=analize_case(cases[i][0], cases[i][1])
		write_output(output_file, print_number_case, switches)
