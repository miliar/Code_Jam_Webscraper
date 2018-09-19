import string

class Alien_Language():
    def __init__(self, filename=''):
        self.file=filename
        self.length_words=0
        self.length_language=0
        self.case_num=0
        self.language=[]
        self.cases={}

    def open_file(self):
        fs = open(self.file)
        section_num=1
        line_cnt=1
        for line in fs:
            if line[0].isdigit():
                l=line.split()
                self.length_words=int(l[0])
                self.length_language=int(l[1])
                self.case_num=int(l[2])
            else:
                #print section_num
                #print line_cnt
                #print self.length_language
                #print line_cnt>self.length_language
                if section_num==1 and line_cnt>self.length_language:
                    section_num+=1
                    line_cnt=1
                elif section_num==1 and line_cnt<=self.length_language:
                    line=line.strip()
                    self.language.append(line.strip())
                    line_cnt+=1
                    
                if section_num==2 and line_cnt>self.case_num:
                    fs.close()
                    return
                elif section_num==2 and line_cnt<=self.case_num:
                    line=line.strip()
                    e=[]
                    temp=''
                    for char in line:
                        if char.isalpha() and not temp:
                             e.append(char)
                        elif char==')':
                            e.append(temp[1:])
                            temp=''
                        else:
                            temp+=char
                    #self.cases[1]=[cases senario, cnt of occurence]
                    self.cases[line_cnt]=[tuple(e), 0]
                    line_cnt+=1
                    
            #print self.length_words
            #print self.length_language
            #print self.case_num
            #print self.language
            #print self.cases
            #print ''

    def find_cnt(self):
        for c_num, c in self.cases.items():
            self.find_pattern(c_num, c[0], c[1])
        fi=open('codejam2009_solutionA.txt', 'w')
        for c_num, data in self.cases.items():
            s='Case #'+str(c_num)+': '+str(data[1])+'\n'
            fi.write(s) 
        fi.close()
        
    def find_pattern(self, c_num, pattern, cnt):
        #print pattern
        #print len(pattern)
        #print cnt
        
        words=self.language[:]
        #print words
        n=0
        while n<self.length_words:
            #print words
            #print pattern[n]
            #print n
            t=[]
            for word in words[:]:
                #print word
                if word[n] in pattern[n]:
                    t.append(word)
            words=t
            n+=1
        self.cases[c_num][1]=len(words)
        #print words



A=Alien_Language('A-small-attempt0.in')
A.open_file()
A.find_cnt()
