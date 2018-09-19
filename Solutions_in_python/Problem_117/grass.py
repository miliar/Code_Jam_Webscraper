def read_num():
    string=file.readline()
    list=string.rstrip("\n").split()
    num_line=int(list[0])
    return num_line



def row_valid(block,row,column):
    maximum=max(block[row])
    if block[row][column]<maximum:
        return 0
    else:
        return 1

def column_valid(block,row,column):
    if row_valid(block,row,column):
        return 1
    else:
        return 0
            


def is_valid(block,l1,row,column):
    if row_valid(block,row,column) or column_valid(l1,column,row):
        return 1
    else:
        return 0

def maximum(block):
    max_list=[]
    for row in block:
        max_list.append(max(row))
    return max(max_list)
    
           
m=[]
l=[]
count=0
n=0
case=1
file=open("small.in","r")
num_case=int(file.readline())
num_line=read_num()
while count<num_line:
    line=file.readline()
    line=line.rstrip("\n").split()
    m.append(line)
    count+=1
    if len(m)==num_line and n<num_case:
        l.append(m)
        count=0
        m=[]
        n+=1
        if len(l)<num_case:
            num_line=read_num()
file.close()
text=open("output.txt","a")
for block in l:
    final=[]
    max_num=maximum(block)
    l1=[]
    for column in range(0,len(block[0])):
        column_list=[]
        for row in block:
            column_list.append(row[column])
        l1.append(column_list)
    for num_row in range(0,len(block)):
        for num_column in range(0,len(block[0])):
            if block[num_row][num_column]!=max_num:
                if is_valid(block,l1,num_row,num_column):
                    final.append("True")
                else:
                    final.append("False")
    if "False" in final:
        text.write("Case #%d: NO\n"%case)
        case+=1
    else:
        text.write("Case #%d: YES\n"%case)
        case+=1
       
