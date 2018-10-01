import re
f_in = open('A-small-attempt10.in','r')
#f_in = open('test.in','r')

line_number=0
length=0
words=[]
words_number=0
patterns=[]
pattern_number=0
#initial file
for line in f_in:
    line_number+=1
    if line_number==1:
        length,words_number,pattern_number=line.split(' ')
    elif line_number>1 and line_number<=(int(words_number)+1):
        words.append(line[0:int(length)])
    elif line_number>(int(words_number)+1) and line_number<=(int(pattern_number)+int(words_number)+1):
        patterns.append(line.strip())

print 'length='+length
print 'words number='+words_number
print 'pattern_number='+pattern_number

print words
print patterns

f_out=open('A-small.out','w')        
alien_lan = re.compile(r'\(\w+\)|\w')
token = re.compile('\w')
test_counter=0
for pattern in patterns:
    match_words=[]
    counter=0
    pattern_info = alien_lan.findall(pattern)
    info_index=-1
    for info in pattern_info:
        info_index+=1
        if info.find("(")!=-1:
            pattern_info[info_index]=token.findall(info)
    print 'pattern_info='+str(pattern_info)
    for word in words:
        test_counter+=1	
        satisfy=True
        word_token = token.findall(word)
        print word_token
        token_index=-1
        for single_word in word_token:
            token_index+=1            		
            if single_word not in pattern_info[token_index]:
                satisfy=False
                break
            else:
                print 'single word='+ single_word
        if satisfy == True:
            if word not in match_words:
                match_words.append(word)
                counter+=1
    f_out.write('Case #'+str(patterns.index(pattern)+1)+': '+str(counter)+'\n')
f_out.close()
f_in.close()
print test_counter