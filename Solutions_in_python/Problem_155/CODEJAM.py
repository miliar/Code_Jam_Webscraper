def sol():
    #read input
    global line_counter
    aud = inp[line_counter].split(' ')
    line_counter+=1
    #code
    no_of_friends = 0
    no_standing = 0
    for min_standing in range(int(aud[0])+1):
        i = int(aud[1][min_standing])
        if (no_standing < min_standing):
            no_of_friends += min_standing-no_standing
            no_standing = min_standing
        no_standing += i
    return str(no_of_friends)
    

with open('A-large.in', 'r') as f:
    inp = f.readlines()
    f.close()
line_counter = 0
T = int(inp[line_counter])
line_counter+=1
data = ''
for i in range(T):
    data += 'Case #%d:' %(i+1) + ' ' + sol()+'\n'
with open('output.txt', 'w') as f:
    f.write(data)
    f.close()
print data
print 'done!'
