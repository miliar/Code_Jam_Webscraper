def solve(combine, opposed, invoke):
	elList = ""
	
	for c in invoke:
		elList += c
		if len(elList) >= 2:
			for combo in combine:
				if elList[-2:] == combo[0:2] or elList[-2:] == combo[1::-1]:
					elList = elList[:-2] + combo[2]
			# check for opposing elements
			for op in opposed:
				if elList.find(op[0]) != -1 and elList.find(op[1]) != -1:
					elList = ""
	
	res = []
	for c in elList:
		res += [ c ]
	return str(res).replace("'", "")

if __name__ == "__main__":
	print solve([ "QRI" ], [ ], "RRQR")
	#rint solve([ "QFT" ], [ "RF" ], "QF")
	#rint solve([ "QFT" ], [ "RF" ], "QEF")
	#rint solve([ "QFT" ], [ "RF" ], "RFE")
	#rint solve([ "QFT" ], [ "RF" ], "REF")
	#rint solve([ "QFT" ], [ "RF" ], "RQF")
	#rint solve([ "QFT" ], [ "RF" ], "RFQ")
