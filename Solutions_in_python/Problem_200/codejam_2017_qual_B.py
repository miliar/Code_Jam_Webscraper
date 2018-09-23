def change_to_nine(string,i):

    for j in range(i+1,len(string)):
        string = string[:j]+'9'+string[j+1:]

    return string


def change_to_lower(string,i):
    flag = True
    for j in range(i,0,-1):
        flag = False
        if int(string[j])>int(string[j-1]):
            string = string[:j]+str(int(string[j])-1)+string[j+1:]
            break
        if string[j]==string[j-1]:
            string = string[:j]+'9'+string[j+1:]
            flag = True
    if flag:
        string = str(int(str(int(string[0])-1)+string[1:]))
    return string

for tc in range(1,int(raw_input())+1):
    string = raw_input()

    for i in range(len(string)-1):
        if int(string[i])>int(string[i+1]):
            string = change_to_nine(string,i)
            string = change_to_lower(string,i)
            break
    print "Case #"+str(tc)+": "+string
