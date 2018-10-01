import math
fw = open('g.txt', 'w')
fr = open('D-small-attempt0.in', 'r')
t=int(fr.readline())
for k in range(1,t+1):
    s=[]
    s=fr.readline().split()
    if s[0]=='1':
        fw.write('Case #'+str(k)+': GABRIEL'+'\n')
    elif s[0]=='2':
        if (int(s[1])*int(s[2]))%2==0:
            fw.write('Case #'+str(k)+': GABRIEL'+'\n')
        else:
            fw.write('Case #'+str(k)+': RICHARD'+'\n')
    elif s[0]=='3':
        if (s[1]=='2' and s[2]=='3') or (s[1]=='3' and s[2]=='2') or (s[1]=='3' and s[2]=='3') or (s[1]=='4' and s[2]=='3') or (s[1]=='3' and s[2]=='4'):
            fw.write('Case #'+str(k)+': GABRIEL'+'\n')
        else:
             fw.write('Case #'+str(k)+': RICHARD'+'\n')
    elif s[0]=='4':
        if (s[1]=='4' and s[2]=='3') or (s[1]=='3' and s[2]=='4') or (s[1]=='4' and s[2]=='4'):
            fw.write('Case #'+str(k)+': GABRIEL'+'\n')
        else:
             fw.write('Case #'+str(k)+': RICHARD'+'\n')
fw.close()
fr.close()

             
            
