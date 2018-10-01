import codecs

with codecs.open('A-small-attempt2.in','r','utf-8') as f_in:
    for j in range(int(f_in.readline())):
        row_1 = f_in.readline().strip()
        cards_1 = list()
        for i in range(4):
            cards_1.append(f_in.readline().strip().split(' '))
        row_2 = f_in.readline().strip()
        cards_2 = list() 
        for i in range(4):
            cards_2.append(f_in.readline().strip().split(' '))
        
        cnt = 0
        val = ''
        for el in cards_1[int(row_1)-1]:
            if el in cards_2[int(row_2)-1]:
                cnt += 1
                val = el
        
        if(cnt == 1):
            print('Case #%d: %s' % (int(j)+1, val))
        elif(cnt == 0):
            print('Case #%d: Volunteer cheated!' % (int(j)+1))
        else:
            print('Case #%d: Bad magician!' % (int(j)+1))

        