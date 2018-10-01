#!/usr/bin/env python
import argparse
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input","-i", help="input file")
    parser.add_argument("--output","-o")
    args = parser.parse_args()
    return args

def tidy_num(num):
    if len(num) == 1:
        return num
    nums = list(num)
    already_decrease = False
    special_case = False
    flag = True
    for i in range(len(num)-1):
        if nums[i]> nums[i+1]:
            nums[i+1] = "9" # reassign the maximum value 
            # check if special case, special case only happen once
            if not special_case:
                for j in range(i,-1,-1):
                    if nums[j]!="1":
                        flag = False
                if flag:
                    special_case = True
            if flag and special_case:
                for j in range(i,0,-1):
                    nums[j]="9"
                nums[0] = "0"
                already_decrease = True
                flag = False
            else:      
                if not already_decrease:
                    nums[i] = str(int(nums[i])-1)
                    already_decrease = True
                # looping and decrease the before i+1:
                for j in range(i,0,-1):
                    if nums[j-1]<= nums[j]:
                        break
                    if nums[j-1]> nums[j]:
                        if nums[j-1] != "1":
                            if already_decrease:
                                nums[j] = "9"
                                nums[j-1] = str(int(nums[j-1])-1)
                        else:
                            if j-1:
                                nums[j-1] = "9"
                            else:
                                nums[j-1] = "0"
    print (num,"".join(nums))
    return int("".join(nums))
if __name__ == "__main__":
    arguments = get_arguments()
    output    = arguments.output
    input     = arguments.input
    infile    = open(input,"r")
    outfile   = open(output,"w")
    test      = int(infile.readline().strip())
    for i in range(1,test+1):
        num = infile.readline().strip()
        outfile.write("Case #{}: {}\n".format(i,tidy_num((num))))
    infile.close()
    outfile.close()


    

