def commonstart():
    fin=open(r'C:\Users\Administrator\Desktop\google jam\2014\Deceitful War\D-large.in','r')
    fout=open(r'C:\Users\Administrator\Desktop\google jam\2014\Deceitful War\D.out','w')
    return fin,fout
fin,fout=commonstart()
num=int(fin.readline())
for line in range(0,num):
    length=int(fin.readline())
    Naomi=list(map(float,fin.readline().split()))
    Ken=list(map(float,fin.readline().split()))
    Naomi.sort()
    Ken.sort()
    Ken_min_index=0
    Naomi_trick=0
    Ken_point=0
    for each in Naomi:
        if each<Ken[Ken_min_index]:
            continue
        else:
            Naomi_trick+=1
            Ken_min_index+=1
    Naomi_min_index=0
    for each in Ken:
        if each<Naomi[Naomi_min_index]:
            continue
        else:
            Ken_point+=1
            Naomi_min_index+=1
    Naomi_not_trick=length-Ken_point
    print('Case #%s: %s %s'%(line+1,Naomi_trick,Naomi_not_trick),file=fout)
fin.close()
fout.close()
