inpfile = open('C:/Users/Dane/Desktop/CJ/D-large.in','r')


def sorting(list1):
    for x in range (0, len(list1) -1):
        for y in range (x+1, len(list1)):
            if list1[y] > list1[x]:
                temp = list1[x]
                list1[x] = list1[y]
                list1[y] = temp
    
    return list1

def war( list1, list2,loop):
    count = 0
    for x in range(0,loop):
        if list1[x] < list2[x]:
            count +=1
    
    return count

def Dwar(list1,list2,count):
    while (len(list1) > 0):
        if isonebigger(list1[0],list2) and list1[0] < list2[0]:
            list1.pop(-1)
            list2.pop(0)
        elif list1[0] > list2[0]:
            list1.pop(0)
            list2.pop(0)
            count += 1
        else:
            list1.pop(0)
            list2.pop(0)
    return count

def isonebigger(num1,list1):
    for x in list1:
        if num1 > x:
            return True
    return False

def war( list1, list2,count1):
    while (len(list1) > 0):
        if list2[0] > list1[0]:
            list1.pop(0)
            list2.pop(0)
        else:
            list1.pop(0)
            list2.pop(-1)
            count1 += 1
    return count1
       
        
            
        
def main():
    Naomi = []
    Naomi2 = []
    Ken= []
    Ken2 = []
    
    loop = int(inpfile.readline())
    
    for i in range(0,loop):
        sets = int(inpfile.readline())
        NaomiTxt = inpfile.readline()
        Kentxt = inpfile.readline()
        NaomiTxLs = NaomiTxt.split()
        Kentxls = Kentxt.split()
        for x in range(0,sets):
            Naomi += [float(NaomiTxLs[x])]
            Naomi2 += [float(NaomiTxLs[x])]
            Ken += [float(Kentxls[x])]
            Ken2 += [float(Kentxls[x])]
        Naomi = sorting(Naomi)
        Ken= sorting(Ken)
        Naomi2 = sorting(Naomi2)
        Ken2 = sorting(Ken2)

        
        
        with  open('C:/Users/Dane/Desktop/CJ/output4large.txt','a') as out1:
            out1.write('Case #%d: %d %d' % (i+1,Dwar(Naomi,Ken,0),war(Naomi2,Ken2,0)))
            out1.write('\n')
            
    
main()
