#solution for problem A - Google Code Jam 2012

Afile = open('A-small-attempt0.in', 'r')
T = int(Afile.readline())
Data = []
Data = Afile.readlines()
Result = Data
Result2 = Data
Afile.close()

print Data
print len(Data[0])
print len(Data[1])
print len(Data[2])
sentence1 = Data[0]
print sentence1[1]
sentence2 = list(sentence1)
print sentence2
sentence3 = "".join(sentence2)
print sentence3
print ord("i")
print ord("a")

#translator array from googlerese to english - 1st try
Translator1 = ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','q','t','n','w','j','p','f','m','a','z']
Translator2 = ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']

print Translator1[1]

sentence = [] #temp sentence holder
sentence2 = []
i = 0 #outer count
n = 0 #sentence length
j = 0 #inner count  
letter = 0

while (i < T):
    sentence = list(Data[i])
    sentence2 = list(Data[i])
    n = len(sentence)
    j=0
    letter = 0
    while (j < (n-1)):
        letter = ord(sentence[j])
        if (letter == 32):
            sentence[j] = " " 
            sentence2[j] = " "
        else:
            sentence[j] = Translator1[(letter-97)]
            sentence2[j] = Translator2[(letter-97)]
        j = j+1
    Result[i] = "".join(sentence)
    Result2[i] = "".join(sentence2)
    i = i + 1

print Result
    
c = 0
RFile = open("A-result1.txt", 'w')
while (c < T):
    RFile.write("Case #%d: %s" %(c+1,Result[c]))
    c = c + 1
RFile.close()

c = 0 
RFile = open("A-result2.txt", 'w')
while (c < T):
    RFile.write("Case #%d: %s" %(c+1,Result2[c]))
    c = c + 1
RFile.close()


