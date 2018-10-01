INPUT = "B-small-attempt0.in"
OUTPUT = "B-small-attempt0.out"
NEWLINE = "\n"
  
if __name__ == '__main__':
    in_file = file(INPUT, "r")
    out_file = file(OUTPUT, "w")
    
    lines = in_file.readlines()
    cases_num = int(lines[0])
    
    out_lines = []
    data = lines[1:]    
    for case in range(1 , cases_num+1):
        i = case - 1
        nums = data[i]
        nums = nums.strip().split(" ")
        nums = [int(j) for j in nums]
        A = nums[0]
        B = nums[1]
        K = nums[2]
        
        res = 0
        for t1 in range(A):
            for t2 in range(B):
                if t1 & t2 < K:
                    res += 1
        
        r = ("Case #%d: %d" % (case,res)) + NEWLINE
        out_lines += r
       
    out_file.writelines(out_lines)
    in_file.close()
    out_file.close()
    print 'done problem B'
        