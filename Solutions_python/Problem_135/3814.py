import sys
sys.stdin = open('C:\progchal\gcj 2014\ip.txt', 'r')
sys.stdout = open('C:\progchal\gcj 2014\op.txt', 'w')

t = int(raw_input())
for i in range(t) :
    p = int(raw_input())
    first = []
    for j in range(4):
        first.append(map(int, raw_input().strip().split()))
    q = int(raw_input())
    second = []
    for j in range(4):
       second.append(map(int, raw_input().strip().split()))
    
    magic = list(set(first[p-1]) & set(second[q-1]))
   
    print "Case #"+str(i+1)+":", 
    if len(magic) == 1 :
        print magic[0]
    elif len(magic) > 1 :
        print "Bad magician!"
    else :
        print "Volunteer cheated!"
