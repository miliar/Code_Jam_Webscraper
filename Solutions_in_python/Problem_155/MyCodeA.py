
with open("/home/ntg/CodeJam/A-small-attempt3.in", "r") as ins:
    array = []
    for line in ins:
        array.append(line.strip())

array = array[1:]

answer = []

###########################


MaxShiness = 0
NumFriends = 0

for i in range(0, len(array)):
    a = array[i][2:]
    for j in range(0, len(a)):
        if (j > MaxShiness and int(a[j]) != 0):
            NumFriends += j - MaxShiness
            MaxShiness += int(a[j]) + NumFriends
            
        else:
            MaxShiness += int(a[j])
        
    answer.append(str(NumFriends)) 
    
    MaxShiness = 0
    NumFriends = 0



##########################

with open("/home/ntg/CodeJam/A-small-attempt2.out", "w") as text_file:
    count = 1
    for i in answer:
        text_file.write("Case #" + str(count) + ": " + i + "\n" )
        count += 1

