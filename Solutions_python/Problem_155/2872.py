def test_case(case_no,s_max, string):
    present = int(string[0])
    extra = 0
    for i in range(1,s_max+1):
        if( present < i):
            extra = extra + i-present
            present = i
        present = present + int(string[i])
    result_string = "Case #"+str(case_no)+": "+str(extra)+"\n"
    print(result_string)
    f_output.write(result_string)
    
f_input = open("A-large.in","r")
f_output = open("outfile.txt","w")
t = int(f_input.readline())
for i in range(1,t+1):
    ip = [i for i in f_input.readline().split()]
    s_max,string = int(ip[0]),ip[1]
    test_case(i,s_max, string)
f_output.close()
