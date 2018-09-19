import os, sys
import copy


def dancing(path=os.path.expanduser("~")+"/"+"gcj/"):
#    fin=open(path+"B-small-attempt0.in", "r")
    if (len(sys.argv) > 1):
        fin=open(path+sys.argv[1], "r")
    fout = open(path+"out2.txt", "w")

    test_cases_count = fin.readline().strip()
    print "No of test characters == %s" % test_cases_count

    for i in range(int(test_cases_count)):
        
         case_string = fin.readline().strip().split(" ")
         n = int(case_string[0])
         s = int(case_string[1])
         p = int(case_string[2])
         scores = case_string[3:]
         count = 0

         for j in range(n):
             num = int(scores[j])
             if ((num/3.0) >= p ):
                 count += 1
             elif num >= p:
                 if ((p-((num-p)/2.0)) <= 1):
                     count += 1
                 elif (((p-((num-p)/2.0)) <= 2) and (s > 0)) :
                     s -= 1
                     count += 1
#         print "Case #" + str(i+1) + ": " + str(count)
                 
         fout.write("Case #" + str(i+1) + ": " + str(count) +"\n" )
    fout.close()
    fin.close()
    

dancing()
