import os


#alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C']

def alien(path=os.path.expanduser("~")+"/"+"/Desktop/jam/"):
    fin=open(path+"A-large.in", "r")
    fout = open(path+"out2.txt", "w")

    test_cases_count = fin.readline().strip().split(" ")
    # print "No of test characters == %s" % test_cases_count[0]
    # print "No of test words == %s" % test_cases_count[1]
    # print "No of test cases == %s" % test_cases_count[2]

    possible_words = []
    
    for i in range(int(test_cases_count[1])):
        possible_words.append(fin.readline().strip())


    for i in range(int(test_cases_count[2])):
        case_string = fin.readline().strip()
        alist = []

        string_len = len(case_string)
        i_count = 0

        while i_count < string_len:
            if i_count == string_len:
                break
            if case_string[i_count] == "(":
                alist.append([])
                i_count += 1

                while case_string[i_count] != ")":
                    
                    alist[-1].append(case_string[i_count])
                    i_count += 1
            elif case_string[i_count] == ")": 
                i_count += 1
            else:
                alist.append([case_string[i_count]])
                i_count += 1


        word_count = 0
        flag = 1
        
        for j in range(int(test_cases_count[1])):
            flag = 1
            for k in range(int(test_cases_count[0])):
                if possible_words[j][k] in alist[k]:
                    pass
                else:
                    flag = 0
                    break
            if (k == int(test_cases_count[0]) - 1) and flag == 1 :
                word_count += 1

        fout.write("Case #"+ str(i+1)+ ": " + str(word_count) + "\n")
    fout.close()
    fin.close()
    

alien()
