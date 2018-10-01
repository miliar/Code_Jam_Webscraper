'''
Created on Apr 14, 2012

@author: arcra
'''

mapped_alphabet = {
'a':'y',
'b':'h',
'c':'e',
'd':'s',
'e':'o',
'f':'c',
'g':'v',
'h':'x',
'i':'d',
'j':'u',
'k':'i',
'l':'g',
'm':'l',
'n':'b',
'o':'k',
'p':'r',
'q':'z',
'r':'t',
's':'n',
't':'w',
'u':'j',
'v':'p',
'w':'f',
'x':'m',
'y':'a',
'z':'q'
}


def SpeakingInTongues(line):
    
    newline = ""
    for char in line:
        if char == ' ':
            newline = newline + ' '
        elif char == '\n':
            newline = newline + '\n'
        else:
            newline = newline + mapped_alphabet[char]
    
    return newline

def Wrapper():
    inputFile = open("A-small-attempt0.in", "r")
    lines = inputFile.readlines()
    inputFile.close()
    
    lines = lines[1:]
    
    caseCount = 1
    outputFile = open("output_SpeakingInTongues.out", "w")
    
    for line in lines:
        result = SpeakingInTongues(line)
        outputFile.write('Case #' + str(caseCount) + ": " + result)
        caseCount = caseCount + 1
    
    outputFile.close()
    
if __name__ == '__main__':
    Wrapper()