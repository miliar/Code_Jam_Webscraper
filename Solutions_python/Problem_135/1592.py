import sys

fname = sys.argv[1]

handler = open(fname, "r")
lines = [line.strip() for line in handler]

testcases_count = int(lines.pop(0))

for case in range(testcases_count):
    answer1 = int(lines.pop(0))
    
    for line in range(1,5):
        cards = lines.pop(0).split(' ')
        if line == answer1: reduced_set = cards
        
    answer2 = int(lines.pop(0))
    
    solution = None
    for line in range(1,5):
        cards = lines.pop(0).split(' ')
        if line == answer2:
            solution = [card for card in reduced_set if card in cards]
            
    if not solution:
        result = "Volunteer cheated!"
    else:
        result = str(solution.pop()) if len(solution) == 1 else "Bad magician!"
	
    print "Case #%d: %s" % (case+1, result)
	
handler.close()