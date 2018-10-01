input = open('B-small-attempt3.in','r')
output = open('output1.txt','w')

numberoftests = int(input.readline())

def permute(word):
         """
         By Barry Carrol <Barry.Carroll at psc.com>
         on Tutor list, revised (last line) by me.
         """
         retList=[]
         if len(word) == 1:
                 # There is only one possible permutation
                 retList.append(word)
         else:
                 # Return a list of all permutations using all characters
                 for pos in range(len(word)):
                         # Get the permutations of the rest of the word
                         permuteList=permute(word[0:pos]+word[pos+1:len(word)])
                         # Now, tack the first char onto each word in the list
                         # and add it to the output
                         for item in permuteList:
                                 retList.append(word[pos]+item)
         #return retList
         return list(set(retList)) # make elements of retList unique

def strip_of_zeros(str):
##    print str
    returnstr = ''
    for i in range(len(str)):
        if str[i] != '0':
            break
        
    for index in range(i,len(str)):
        returnstr += str[index]
        
    return returnstr

for testnumber in range(1,numberoftests+1):
    
##    words = input.readline().split(" ")
    number = input.readline()
    if number[len(number)-1] == '\n':
        number = number[:-1]
        
    permutations = permute(number)
##    permutations.remove(number)
    
    min = 1000000
    print permutations
    for i in range(len(permutations)):
        if int(number)<int(permutations[i]) < min:
            min = int(permutations[i])
    if min != 1000000:
        result = min
    elif len(permutations)!=0:
        permutations.sort()
        newnumber = strip_of_zeros(permutations[0])
        result = int(newnumber[0]+'0'+newnumber[1:])
        i = 1
        while result <= int(number):
            newnumber = strip_of_zeros(permutations[i])
            result = int(newnumber[0]+'0'+newnumber[1:])
            i+=1
            if i >= len(permutations):
                break
    else:
        result = number+'0'

    output.write('Case #'+str(testnumber)+': '+str(result)+'\n')
