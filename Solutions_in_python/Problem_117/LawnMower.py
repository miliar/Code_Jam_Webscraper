#!/user/bin/python

def check_col(data, j, row):   
    temp = []
    for i in range(0,row):
        temp.append(data[i][j])
    temp = list(set(temp))
    if len(temp) == 1:
        return 1
    
def check_row(data, i):   
    temp = data[i]
    temp = list(set(temp))
    if len(temp) == 1:
        return 1

def check_one_test(fo) :
    data = []
    all_hights = []
    n_m = fo.readline().strip().split()
    #print n_m
    for i in range(0,int(n_m[0])):
        temp = list(fo.readline().strip().split())
        num =[]
        for j in range(0,int(n_m[1])):
            num.append(int(temp[j]))
            all_hights.append(int(temp[j]))
        data.append(num)
    all_hights = sorted(list(set(all_hights)))
    
    count = 0
    while 1:
        temp = []
        all_data = []
        for i in range(0,int(n_m[0])):
            temp = list(set(data[i]))
            if len(temp) == 1:
                if all_hights[count] in temp:
                    for j in range(0,int(n_m[1])):
                        if check_col(data, j, int(n_m[0])):
                            pass
                        else:
                            data[i][j] = all_hights[count + 1]
            
        
        for i in range(0,int(n_m[1])):
            temp = []
            for j in range(0,int(n_m[0])):
                temp.append(data[j][i])
            temp = list(set(temp))
            #print temp
            if len(temp) == 1:
                if all_hights[count] in temp:
                    for j in range(0,int(n_m[0])):
                        if check_row(data, j):
                            pass
                        else:
                            data[j][i] = all_hights[count + 1]
            
        for i in range(0,int(n_m[0])):
            temp = list(set(data[i]))
            all_data = all_data + temp
        all_data = list(set(all_data))
        if len(all_data) == 1:
            return 'Y'
        
        count = count + 1
        if count == (len(all_hights) - 1):
            break
    
    #print all_hights
    return 'N'
    #print data

fo = open("input", "r")
fw = open("output", "w")
no_of_cases = int(fo.readline().strip())
#print no_of_cases
count = 1
while no_of_cases:
    ret = ''
    string = ''
    ret = check_one_test(fo)
    print ret
    if ret == 'Y':
        string = "YES"
    else:
        string = "NO"
    fw.write("Case #" + str(count) + ": " + string + "\n")
    no_of_cases =  no_of_cases - 1
    count = count + 1

fo.close
fw.close