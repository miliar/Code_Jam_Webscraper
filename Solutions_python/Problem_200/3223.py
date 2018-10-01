
# coding: utf-8

# In[11]:

import numpy
lines = open('small.input', 'r').read().splitlines()
print lines
Ncases = int(lines[0])
#numberOfCases = int(4)

with open('output.txt', 'w') as out:
    for number in range(Ncases):
        findTidy = lines[number+1]
        while True:
            tidyList = numpy.array(list(findTidy))
            lenth = len(tidyList)
            allNotSet = False
            for i in range(1, lenth):
                if not tidyList[i-1] <= tidyList[i]:
                    tidyList[i-1] = int(tidyList[i-1]) - 1
                    tidyList[i:] = 9
                    allNotSet = True
                    findTidy = list(tidyList)
                    break
            if not allNotSet:
                break
        out.write('Case #{}: {}'.format(number+1, int(''.join(tidyList))))
        out.write('\n')
        print 'Case #{}: {}'.format(number+1, int(''.join(tidyList)))
out.closed


# In[ ]:



