one = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
onet = "our language is impossible to understand"
two = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
twot = "there are twenty six factorial possibilities"
three = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
threet = "so it is okay if you want to just give up"

translate = {}

# print one
# print two

for pair in [[one,onet],[two,twot],[three,threet]]:
    for i in xrange(len(pair[0])):
        try:
            if (translate[pair[0][i]] != pair[1][i]):
                print "uh oh"
        except:
            translate[pair[0][i]] = pair[1][i]

translate['z'] = 'q'
translate['q'] = 'z'
            
for string in "abcdefghijklmnopqrstuvwxyz":
    print string[0],translate[string[0]]

for pair in [[one,onet],[two,twot],[three,threet]]:
    # print pair[0]
    lst=[]
    for i in xrange(len(pair[0])):
        lst.append(translate[pair[0][i]])
    # print "".join(lst) 
    # print pair[1]

def xlate(string):
    lst = []
    for i in xrange(len(string)):
        if (string[i] != '\n'):
            lst.append(translate[string[i]])
    return lst
    
#f = open("ese.small.txt","r")
#f = open("ese.test.txt","r")
#f = open("A-small-attempt0.in","r")
f = open("A-small-attempt1.in","r")

s = f.readline()
n = int(s)

#print "foo"

i = 0
for line in f:
    lst = xlate(line)
    if (line != "\n"):
        i +=1
        print "Case #"+str(i) + ":"+ " " + "".join(lst)


