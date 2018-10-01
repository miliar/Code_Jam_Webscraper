import sys

def file_read(filename):
	f=open(filename)
	engl=[]
	googl=[]
	count=0
	maps={}
        lines=[]
        words=[]

	gl_code="abcdefghijklmnopqrstuvwxyz"
	en_code="yhesocvxduiglbkrztnwjpfmaq"
	maps[' ']=' '
	maps['\n']=''
	
	for i in range(len(gl_code)):
                maps[gl_code[i]]=en_code[i]

        for i in f:
                if count==0:
                        file_len=int(i)
                        count=1
                else:
                        lines.append(i)

        for i in range(file_len):
                
                big_line=""
                big_line+="Case #"+str(i+1)+': '
                for word in lines[i]:
                        for letter in word:
                                big_line+=maps[letter]
                        #big_line+=" "
                print big_line
                
                        
        
        


def main():
	file_read(sys.argv[1])	


if __name__=="__main__":
	main()


