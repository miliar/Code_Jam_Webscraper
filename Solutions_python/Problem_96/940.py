FILENAME = "B-large"
LINE_PER_CASE = 1
INPUT_FILE = "%s.in" % FILENAME
OUTPUT_FILE = "%s.out" % FILENAME

# 1st tier: total score
# 2nd tier: 0 - normal min best, 1 - surprise min best
scores = [[0, -1], [1, -1], [1, 2], [1, 2], [2, 2], [2, 3], [2, 3], [3, 3], [3, 4], [3, 4], [4, 4], [4, 5], [4, 5], [5, 5], [5, 6], [5, 6], [6, 6], [6, 7], [6, 7], [7, 7], [7, 8], [7, 8], [8, 8], [8, 9], [8, 9], [9, 9], [9, 10], [9, 10], [10, 10], [10, -1], [10, -1]]

def solve(lines):
    output = 0
    
    line = lines[0].split(" ")
    
    googlers = int(line[0])
    surprises = int(line[1])
    baseline = int(line[2])
    totals = [int(i) for i in line[3:]]
    
    for i in range(len(totals)):
        if scores[totals[i]][0] >= baseline:
            output += 1
            totals[i] = None
    totals = [total for total in totals if total != None]
    
    for s in range(surprises):
        for i in range(len(totals)):
            if scores[totals[i]][1] >= baseline:
                output += 1
                totals[i] = None
                totals = [total for total in totals if total != None]
                break
        
    return output

if __name__ == '__main__':
    input_file = open(INPUT_FILE, "r")
    output_file = open(OUTPUT_FILE, "w")
    
    cases = int(input_file.readline())
    for case in range(1, cases+1): # Count case from 1, 2, ..., n
        input_lines = list()
        for i in range(LINE_PER_CASE):
            input_lines.append(input_file.readline()[:-1]) # Remove newline
        output_file.write("Case #%d: %s\n" % (
            case,
            solve(input_lines),
        ))
    
    input_file.close()
    output_file.close()
