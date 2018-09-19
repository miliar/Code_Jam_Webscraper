def get_file_as_list(filename):
    with open(filename) as f:
        lines = [line.strip() for line in open(filename)]
    return lines;

def get_audience_members(s_max, thresh_list):
    total_extra_persons = 0
    num_persons_standing = 0
    for i in range(s_max+1):
        if(num_persons_standing<i):
            extra_required = (i-num_persons_standing);
            total_extra_persons += extra_required
            num_persons_standing += extra_required
        num_persons_standing += thresh_list[i]
    return total_extra_persons


lines = get_file_as_list('./A-large.in')
num_test_case = int(lines[0])
output_file = open('lets_clap_output_large.txt', 'w')
for x in range(num_test_case):
    s_max = int(lines[x+1].split()[0])
    thresh_list = map(int, list(lines[x+1].split()[1]))
    #print "case ",x
    total_extra_persons = get_audience_members(s_max, thresh_list);
    print>>output_file,"Case #"+str(x+1)+": "+str(total_extra_persons)
