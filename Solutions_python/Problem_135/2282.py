def solve():
    src_file=open("C:\\Users\\Neo\\Desktop\\Learning Python\\google code jam\\MagicTrick.in")
    rst_file=open("C:\\Users\\Neo\\Desktop\\Learning Python\\google code jam\\MagicTrickResult.txt","a")
    cases=int(src_file.readline())
    for case in range(cases):
        row=int(src_file.readline())
        for i in range(row):
            line=src_file.readline()
        nums1=line.strip().split(" ")
        for i in range(4-row):
            line=src_file.readline()
        row=int(src_file.readline())
        for i in range(row):
            line=src_file.readline()
        nums2=line.strip().split(" ")
        for i in range(4-row):
            line=src_file.readline()
        count=list(set(nums1).intersection(set(nums2)))
        result="Case #"+str(case+1)+": "
        if(len(count)==1):
            result+=str(count[0]).strip()
        elif(len(count)==0):
            result+="Volunteer cheated!"
        else:
            result+="Bad magician!"
        rst_file.write(result+"\n")
    src_file.close()
    rst_file.close()
            
