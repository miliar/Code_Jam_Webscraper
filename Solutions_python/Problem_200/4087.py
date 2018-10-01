import sys

def cat(filename):
        lines = []
        with open(filename) as f:
                for line in f:
                        line = line.replace("\n","")
                        lines.append(int(line))
        return lines

def action(m):
	number = str(m)
	if int(number < 10):
		return int(number)
	else:
		result = ""
		for n in xrange(int(number),1,-1):
        		nstring = str(n)
        		last = int(nstring[0])
        		tidy = 1
			counter = 0
        		while(counter < len(nstring)):
                		if int(nstring[counter]) >= last:
                        		tidy = 1
                		else:
                        		tidy = 0
					break
                		last = int(nstring[counter])
				counter = counter + 1
        		if tidy == 1:
                		result = nstring
		        	return result


if len(sys.argv) > 1:
        inp = cat(sys.argv[1])
        caseNum = 1

        for i in range(1, inp[0] + 1):
                n = inp[i]

                output = action(n)
                if output == "" or output == None:
                        output = n

                print("%s%d%s%s" % ("Case #", caseNum, ": ", str(output)))
                caseNum = caseNum + 1

else:
        print
        print "Please provide a file name for input. \n ( Example: python <script> <input filename> )"
        print

