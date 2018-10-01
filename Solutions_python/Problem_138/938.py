import copy
def main():
	testcases =input()
	ans_dw=[]
	ans_w =[]
	for case in range(0,testcases):
		blocks= input()
		naomi = raw_input()
		ken = raw_input()
		naomi_w = naomi.split()
		ken_w = ken.split()
		naomi_w.sort()
		ken_w.sort()

		#print naomi_w
		#print ken_w 	
	
		dw=0
		w=0
		
		naomi_temp = copy.copy(naomi_w)
		ken_temp = copy.copy(ken_w)

		for i in reversed(naomi_temp): 
			counter =0
			for j in reversed(ken_temp):
				if i > j:
					counter +=1
					ken_temp.remove(j)
					break
			if(counter == 0):
				break
		dw = blocks - len(ken_temp)
		ans_dw.append(dw)
	
		naomi_temp1 = copy.copy(naomi_w)
		ken_temp1 = copy.copy(ken_w)

		for i in naomi_temp1: 
			counter =0
			for j in ken_temp1:
				if j>i:
					counter +=1
					ken_temp1.remove(j)
					break
			if(counter == 0):
				break
		w = len(ken_temp1)
		ans_w.append(w)
		cases = case+1
		print 'Case #'+ str(cases) + ': ' + str(dw) +' ' +str(w)
		case += 1
	

if __name__ == "__main__":
	main()
