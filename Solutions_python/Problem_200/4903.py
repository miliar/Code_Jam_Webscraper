output_file = open("output2.out","w")


def print_result(result):
    global output_file
    global result_printed

    if i>0:
        output_file.write("\n")

    print("Case #"+str(i+1)+": "+str(result))
    output_file.write("Case #"+str(i+1)+": "+str(result))
    result_printed = True


num_testcases = int(raw_input())
cases = []

for _ in range(0, num_testcases):
    case = raw_input()
    cases.append(case)

for i in range(0, num_testcases):
    last = cases[i]
    last_int = int(last)
    result_printed = False

    while not result_printed:
        if last_int<10:
            print_result(last)
        else:
            last_digits = list(last)
            #print(last_digits)
            is_tidy = True
            multiplier = 1
            pos = -1
            for d in range(len(last_digits)-1,0,-1):
                if int(last_digits[d]) < int(last_digits[d-1]):
                    pos = d
                    for dd in range(d+1,len(last_digits)):
                        pos = dd
                        multiplier = multiplier/10
                        if int(last_digits[dd])!=0:
                            break
                    #print("["+str(pos)+"]="+last_digits[pos])
                    last_int = last_int-((int(last_digits[pos])+1)*multiplier)
                    last = str(last_int)
                    #print("last="+last)
                    is_tidy = False
                    break
                multiplier = multiplier*10

            if is_tidy:
                print_result(last)

output_file.close()
