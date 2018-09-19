global count
count = 0

####OPEN FILE####
with open('A-small-attempt1.in','r') as f:
    aud = f.read().split('\n')
    f.close()

aud.pop(0)
lstAud = aud
def findMinimum (ln):
    data = ln.split(' ')
    lstAud = data [1]
    audNeed = 0
    audStand = 0
    count = 0
    for i in lstAud:
        if int(i) == 0:
            count +=1
        elif count <= audStand:
            audStand += int(i)
            count+=1
        else:
            audNeed += count-audStand
            #print 'stand: ' ,audStand
            #print 'need: ', audNeed
            audStand += int(i) + audNeed
            count+=1
    return audNeed
output = ''
for i in lstAud:
    if i != '':
        audNeed = findMinimum(i)
        count +=1
        output+= 'Case #' + str(count)+': ' + str(audNeed) + '\n'
with open('output.txt', 'w') as f:
    f.write(output)
    f.close()
print output