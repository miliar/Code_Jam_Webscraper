'''
Created on 08-Apr-2012

@author: RAJAT
'''
def main():
    a=open('A-small-attempt1.in','r')
    b=open('b.txt','w')
    first=a.readline()
    l=int(first)
    
    s1='''zy qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc
    jv'''
    s2='''qa zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give 
    up'''
   
    for i in range(0,l):
        s3="Case #{}: ".format(i+1)
        s=a.readline()
        for x in s:
            s3+=s2[s1.find(x)]
        b.write(s3)
        b.write('\n')
    
           
            
        
if __name__== '__main__':main()