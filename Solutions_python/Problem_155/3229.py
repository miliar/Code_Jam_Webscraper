import sys
def parse_input(input_file):
    
    num_testcases = int(input_file.readline())
    output = []
    line_num = 1
    for line in input_file:
        line_split= line.split()
        num = int(line_split[0]) 
        numzeros= 0
        count = 0
        track = 0
        for si in line_split[1]:
            if count == 0 and int(si) == 0:
                numzeros += 1
                track += 1
            elif track < count  and count > 0 and int(si) > 0:
                numzeros += abs(count-track)
                track += abs(count-track)
            track += int(si)
            count += 1

        output.append((line_num, numzeros))
        line_num += 1
    return output
                        
def print_output(output):
    for i in output:
        print "Case #%d: %d" % (i[0], i[1]) 

def main():

    input_file = open(sys.argv[1], 'r')
    output = parse_input(input_file)
    print_output(output)


if __name__ == '__main__':
    main()
