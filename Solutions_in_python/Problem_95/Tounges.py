'''
Created on Apr 14, 2012

@author: Nick
'''

inputFile = open('in.txt')
outputFile = open('out.txt','w')

english = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
googlish = ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']

inputTxt = inputFile.readlines()
outputLine = ''

for i in range(1,int(inputTxt[0])+1):
    words = inputTxt[i].split()
    for word in words:
        for letter in word:
            index = english.index(letter)
            outputLine += googlish[index]
        outputLine += ' '
    outputLine += '\n'
    outputFile.write("Case #" + str(i) + ": ")
    outputFile.write(outputLine)
    outputLine = ''
    
    
            