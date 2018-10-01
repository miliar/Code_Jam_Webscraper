
list_cases=[]
list_output=[]
testcases=0
def main():
    input_parser()
    process()
    




def input_parser():
    count=0
    fo = open("C:\\input.txt", "r+")
    testcases = int(fo.readline())
    while count < testcases:
        str_case = fo.readline()
        list_case = str_case.split()
        list_cases.append(str(list_case[1]))
        count = count + 1
    fo.close()

def process():
    count=1
    fo = open("C:\\output.txt", "w+")
    for string_case in list_cases:
        list1=list(string_case)
        result = sub_process(list1)
        string_data = "Case #%d: %d\n" %(count, result)
        fo.write(string_data)
        count=count+1
    fo.close()

def sub_process(list1):
    count=total=temp=result=prev_total=0
    length = len(list1)
    while count < length:
        temp = int(list1[count])
        total = temp + total
        if temp and ( (count) > prev_total):
            result =  result + (count)-prev_total
            total = total + result
        prev_total = total
        count = count+1
    return result


main()


    
