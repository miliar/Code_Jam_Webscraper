def read_words(filename):
    '''
    converts a file to a list
    '''
    
    words = []
    for line in filename:
            words.append(line.split())
    return words

filename = open("test2.txt", "r")
T= int(filename.readline())
total = read_words(filename)

for i in range(len(total)):
    count = 0
    first = int(total[i][0])
    second = int(total[i][1])
    if first<=1 and second>=1:
        count+=1
    if first<=4 and second>=4:
        count+=1
    if first<=9 and second>=9:
        count +=1
    if first<=121 and second>=121:
        count +=1
    if first<=484 and second>=484:
        count +=1
    print "Case #"+str(i+1)+ ": " + str(count)