# Small helper functions for file IO
# Written for Google CodeJam 2017
# Author: Daniel Ruland

import os

def get_dataset(fname = "A-large.in"):
	f = load_input_file(fname)
	dataset = parse_datafile(f)
	return dataset

def load_input_file(fname):
	os.chdir("/home/thareal/Downloads")
	cwd = os.getcwd()
	fpath = cwd +"/" + fname
	input_file = open(fpath, 'r')
	input_file.seek(0)
	
	print "[+] Input file opened successfully!"	
	return input_file


def parse_datafile(datafile):
	line1 = datafile.readline()
	n = int(line1.strip())
	
	i = 0
	data_array = []
	raw_data = datafile.readline()
	data = raw_data.strip()
	
	while raw_data != '':
		i += 1
		data_array.append(data)
		raw_data = datafile.readline()
		data = raw_data.strip()
		
	print "Length: %s" % i
	return data_array	
	
	
def create_output_file():
	os.chdir("/home/thareal/Downloads")
	cwd = os.getcwd()
	fpath = cwd +"/" + "output-A_large.txt"
	output_file = open(fpath, 'w')
	output_file.seek(0)
	
	print "[+] Output file created successfully!"	
	return output_file

