#@author slolean
#a magic trick

#import sys

#lines = sys.stdin.readlines()

def input_cases():
	T = input()#test cases
	#case_num = []
	rows = []
	result_row = []
	for i in range(T):
		#case_num.append(i+1)
		#result_row = []
		for j in range(2):#for both the cases
			row = input()#row value
			#row_list = []
			#row_list.append(row)
			for k in range(4):
				result = []
				c_seq = raw_input()
				for itm in c_seq.split():
					result.append(itm)
				result_row.append(result)
			rows.append(row)
	#print case_num
	#print case_num
	#print rows
	#print result_row
	
	#print len(rows)
	#print len(result_rows)
	#case_num = 0
	#count = 0#flag
	for i in range(0,T):
		#count = 0#flag
		#case_num+=1
		val = []
		a = rows[2*i]
		b = rows[2*i+1]
		#print a
		#print b
		l1 = result_row[8*i:8*i+4][a-1]
		l2 = result_row[8*i+4:8*i+8][b-1]
		#print result_row[4*i:4*i+4][a-1][a-1]
		#print l1
		#print l2
		#index1 = 4*i+a-1
		#index2 = 4*i+b+3##4-1
		val = [itm for itm in l1 if itm in l2]
		#print val
		#print len(val)
		if len(val)==1:
			result_str = val[0]
		elif len(val)==0:
			result_str = 'Volunteer cheated!'
		else:
			result_str = 'Bad magician!'
		#print result_str
		#print 'Case #'
		#case = i+1
		print 'Case #%i: %s'%(i+1,result_str)


	
def main():
	input_cases()
	
if __name__ == '__main__':
	main()	
