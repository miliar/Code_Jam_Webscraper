import sys

args = sys.argv[1:]
fname = args[0]

f = open(fname)

# read first line for T
T = f.readline().strip()
T = int(T)

for t in range(T):
    table =  f.readline().strip()
    table += f.readline().strip()
    table += f.readline().strip()
    table += f.readline().strip()

    f.readline()

    # print "%d %s" % (t, table)

    # check horizontals
    if all([el == "O" or el == "T" for el in table[0:4]]):
    	print "Case #%d: O won" % (t+1)
    	continue
    if all([el == "O" or el == "T" for el in table[4:8]]):
    	print "Case #%d: O won" % (t+1)
    	continue
    if all([el == "O" or el == "T" for el in table[8:12]]):
    	print "Case #%d: O won" % (t+1)
    	continue
    if all([el == "O" or el == "T" for el in table[12:16]]):
    	print "Case #%d: O won" % (t+1)
    	continue

    if all([el == "X" or el == "T" for el in table[0:4]]):
    	print "Case #%d: X won" % (t+1)
    	continue
    if all([el == "X" or el == "T" for el in table[12:16]]):
    	print "Case #%d: X won" % (t+1)
    	continue

    # check verticals
    if all([el == "O" or el == "T" for el in table[0:16:4]]):
    	print "Case #%d: O won" % (t+1)
    	continue
    if all([el == "O" or el == "T" for el in table[1:16:4]]):
    	print "Case #%d: O won" % (t+1)
    	continue
    if all([el == "O" or el == "T" for el in table[2:16:4]]):
    	print "Case #%d: O won" % (t+1)
    	continue
    if all([el == "O" or el == "T" for el in table[3:16:4]]):
    	print "Case #%d: O won" % (t+1)
    	continue

    if all([el == "X" or el == "T" for el in table[0:16:4]]):
    	print "Case #%d: X won" % (t+1)
    	continue
    if all([el == "X" or el == "T" for el in table[1:16:4]]):
    	print "Case #%d: X won" % (t+1)
    	continue
    if all([el == "X" or el == "T" for el in table[2:16:4]]):
    	print "Case #%d: X won" % (t+1)
    	continue
    if all([el == "X" or el == "T" for el in table[3:16:4]]):
    	print "Case #%d: X won" % (t+1)
    	continue

    # check diagonals
    if all([el == "O" or el == "T" for el in table[0:16:5]]):
    	print "Case #%d: O won" % (t+1)
    	continue
    if all([el == "O" or el == "T" for el in table[3:13:3]]):
    	print "Case #%d: O won" % (t+1)
    	continue

    if all([el == "X" or el == "T" for el in table[0:16:5]]):
    	print "Case #%d: X won" % (t+1)
    	continue
    if all([el == "X" or el == "T" for el in table[3:13:3]]):
    	print "Case #%d: X won" % (t+1)
    	continue

    # check finished
    if any([el == "." for el in table]):
    	print "Case #%d: Game has not completed" % (t+1)
    	continue
    print "Case #%d: Draw" % (t+1)
    
