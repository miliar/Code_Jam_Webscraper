sample = open('C-small-attempt0.in')
line = []
data = []
while sample:
    next_line = sample.readline()
    if next_line == "":
        break 
    else:
        line.append(next_line)
for num_set in line:
    new_set = num_set.rstrip().split(" ")
    int_set = []
    for nums in new_set:
        nums = int(nums)
        int_set.append(nums) 
    data.append(int_set)

n_set= data[0]
n = n_set[0]


outfile = open('results.txt', 'w')

for number in xrange(1,n+1):
    case = data[number]
    lower = case[0]
    upper = case[1]
    num_list = []
    group_list = []
    for count in xrange(lower, upper + 1):
        num_list.append(str(count))
    for str_num in num_list:
        
        group = []
        matches = 0
        for digit in xrange(1,len(str_num)):
            if int(str_num[digit:]+str_num[:digit])>int(str_num) and int(str_num[digit:]+str_num[:digit])<=upper:
                if matches==0:
                    group.append(str_num)
                    matches = 1
                group.append(str_num[digit:]+str_num[:digit])
        if len(group)>1:
               group_list.append(group)

    #print group_list, lower, upper
    total_pairs = 0
    for complete_group in group_list:
        len_group = len(set(complete_group))
        pairs = sum(xrange(len_group))
        total_pairs += len_group-1
    #print total_pairs
    #print
    outfile.write("Case #%d: %d\n" %(number, total_pairs))
    

outfile.close()
print('finished')
    
    
            
        
                
        
        
    
