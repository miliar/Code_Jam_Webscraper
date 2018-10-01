# -*- coding: utf-8 -*-
INPUT  = ["B-small.in","B-large.in"]
OUTPUT = ["Watersheds-small.out","Watersheds-large.out"]
DEBUG  = 0
RUN    = 1
DIRECTIONS = [[-1,0],[0,-1],[0,1],[1,0]]

if DEBUG > 6:
	import time
	
def importData(run):
	input = open(INPUT[run],"r")
	var_T = int(input.readline()[:-1])
	return input,var_T

def importMap(input):
	line = input.readline()[:-1].split(" ")
	map = []
	max_line = []
	
	var_H = int(line[0])
	var_W = int(line[1])
	
	for i in xrange(var_W+2):
		max_line.append(10000)
	
	map.append(max_line)
	for lines in xrange(var_H):
		map_line = [10000]
		line = input.readline()
		if DEBUG > 0:
			print line
		if line.find("\n")!=-1:
			line=line[:-1]
		line = line.split(" ")
		if DEBUG > 0:
			print line
		for height in line:
			map_line.append(int(height))
		map_line.append(10000)
		map.append(map_line)
	map.append(max_line)
	return map,var_H,var_W

def initialBasin_map(var_H,var_W):
	map_basin = []
	map_basin_max = []

	for column in xrange(var_W+2):
		map_basin_max.append(100)
	
	map_basin.append(map_basin_max)
	for line in xrange(var_H):
		map_basin_line=[100]
		for column in xrange(var_W):
			map_basin_line.append(-1)
		map_basin_line.append(100)
		map_basin.append(map_basin_line)
	map_basin.append(map_basin_max)
	return map_basin
	
def getHighestPoint(map,var_H,var_W,map_basin):
	line = 1
	max = -1
	max_line,max_column = -1,-1
	while line <= var_H:
		column = 1
		while column <= var_W:
			if map_basin[line][column]<0 and map[line][column]>max :
				max = map[line][column]
				max_line,max_column = line,column
			column+=1
		line+=1
	return max,max_line,max_column	

def getOutFlow(map,line,column):
	min = map[line][column]
	min_line,min_column = -1,-1
	for direction in DIRECTIONS:
		line_n = line + direction[0]
		column_n = column + direction[1]
		if map[line_n][column_n] < min:
			min = map[line_n][column_n]
			min_line,min_column = line_n,column_n
	return min,min_line,min_column

def getBasin(map,map_basin,var_H,var_W,source,source_line,source_column,basins):
	map_basin[source_line][source_column]=basins
	path = [[source_line,source_column]]
	while path != []:
		next,next_line,next_column = getOutFlow(map,path[0][0],path[0][1])
		if DEBUG > 0:
			print "\n"
			print "Next :",next," (",next_line,",",next_column,")"
			print "Path :",path
			print "Basin:",map_basin
		if next != -1 and next_line > 0 and next_column > 0:
			if map_basin[next_line][next_column]<0:
				path.append([next_line,next_column])
				map_basin[next_line][next_column]=map_basin[path[0][0]][path[0][1]]
			else:
				old_basin = map_basin[path[0][0]][path[0][1]]
				new_basin = map_basin[next_line][next_column]
				basins-=1
				changeBasin(map,map_basin,old_basin,new_basin,path[0][0],path[0][1])
		path.pop(0)
	return basins

def changeBasin(map,map_basin,old_basin,new_basin,line,column):
	path = [[line,column]]
	while path != []:
		map_basin[path[0][0]][path[0][1]] = new_basin
		for direction in DIRECTIONS:
			line_n = path[0][0] + direction[0]
			column_n = path[0][1] + direction[1]
			if map_basin[line_n][column_n] == old_basin:
				path.append([line_n,column_n])
		path.pop(0)

def convertBasin(map_basin,var_H,var_W):
	line = 1
	exchanged = {}
	current = 'a'
	if DEBUG > 0:
		print "Converting: ",map_basin
	map_basin_exchanged = []
	while line <= var_H:
		column = 1
		exchange_line = []
		while column <=var_W:
			temp = map_basin[line][column]
			if temp in exchanged.keys():
				exchange_line.append(exchanged.get(temp)+' ')
			else:
				exchanged[temp]=current
				exchange_line.append(exchanged.get(temp)+' ')
				current = chr(ord(current)+1)
			column += 1
		exchange_line[-1]=exchange_line[-1][0]
		map_basin_exchanged.append(exchange_line)
		line += 1
	return map_basin_exchanged

def outputF(map_basin,var_H,var_W,var_K,output,basins):
	output.write("Case #"+str(var_K+1)+":\n")
	toWrite = convertBasin(map_basin,var_H,var_W)
	for line in xrange(len(toWrite)):
		for column in xrange(len(toWrite[line])):
			output.write(toWrite[line][column])
		output.write("\n")
		output.flush()


def testCase(var_K,input,output):
	basins = 0
	map,var_H,var_W = importMap(input)
	map_basin = initialBasin_map(var_H,var_W)
	while(True):
		source,source_line,source_column = getHighestPoint(map,var_H,var_W,map_basin)
		if source == -1:
			break
		basins = getBasin(map,map_basin,var_H,var_W,source,source_line,source_column,basins)
		basins += 1
	if DEBUG > 0:
		print "Map Basin --- ",map_basin
		print "\n\n\n############ New Case"
	outputF(map_basin,var_H,var_W,var_K,output,basins)
	

input, var_T = importData(RUN)
output = open (OUTPUT[RUN],"w")
for k in xrange(int(var_T)):
	testCase(k,input,output)
