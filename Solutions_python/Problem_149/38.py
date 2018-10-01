
def get_line():
    return raw_input().strip()

formatIntegerList = lambda s: list(map(int,s.split(' ')))

def standard_input():
    T = int(get_line())
    for i in range(T):
        N = int(get_line())
        nums = formatIntegerList(get_line())
        yield (i+1,nums)
        
def handle_case(case):
    nums = case
    lb,rb = 0,len(nums)-1
    result = 0
    #print nums[lb:rb+1]
    while lb < rb:
        mi = min(range(lb,rb+1), key=lambda ind:nums[ind])
        m = nums[mi]
        ld, rd = mi - lb, rb - mi
        #print mi, m, ld, rd
        if ld < rd:
            nums[lb+1:mi+1] = nums[lb:mi]
            nums[lb] = m
            lb += 1
        else:
            nums[mi:rb] = nums[mi+1:rb+1]
            nums[rb] = m
            rb -= 1
        result += min(ld,rd)
            
    return str(result)
    
        
def main():
    for i,case in standard_input():
        print "Case #%d: %s" %(i,handle_case(case))        

if __name__ == '__main__':
    main()
    