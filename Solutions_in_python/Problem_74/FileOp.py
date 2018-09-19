'''
Created on Apr 12, 2011

@author: vipyati
'''

class FileRead :
    
    def __init__(self,fileName='input'):
        self.f=open('D:\Personal\codejam\\'+ fileName+'.in')
        self.line = [];
    
    def getFile(self):
        return self.f
    
    def INT(self):
        self.check()
        return int(self.line.pop(0))

    def LONG(self):
        self.check()
        return long(self.line.pop(0))
 
    def STR(self):
        self.check()
        return str(self.line.pop(0))
    
    def READLINE(self):
        return self.f.readline().rstrip('\n')
  
    def INTG(self,n):
        return [int(self.line.pop(0)) for x in range(n)]     
        
    def check(self):     
        if(len(self.line)==0):
            self.line = self.f.readline().split()   


class FileWrite:
     
    def __init__(self,fileName='out'):
        self.name = 'D:\Personal\codejam\\'+fileName+'.out'
        self.f=open(self.name,'w')
    
    def write(self,s):
        self.f.write(s)
        self.f.write('\n')
        print s
        print '\n'

    def writeCase(self,t,v):
        self.f.write('Case #'+str(t)+': '+str(v))
        self.f.write('\n')
        print 'Case #'+str(t)+': '+str(v)
        print '\n'
       
        