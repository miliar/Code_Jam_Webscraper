import sys

def compute(engines,keywords):
    start = 0
    end = len(keywords)
    max_run_length = 0
    choosen_one = []
    while(start <= len(keywords)-1):
        engine_keyword= {}
        for engine in engines:
            position = 0
            for i in range(start,end):
                if engine != keywords[i]:
                    position = position + 1
                else:
                    break
            engine_keyword[position] = engine
            #print "engine",engine_keyword,start
        max_run_length = max(engine_keyword.keys())
        start = start + max_run_length
        choosen_one.append(engine_keyword[max_run_length])
        #print "choosen one",choosen_one
    return (len(choosen_one)-1)
       
def process_file(f):
    input_count = int(f.readline())
    for i in range(input_count):
        no_of_engines = int(f.readline().strip()) 
        engines = no_of_engines*[""]
        for j in range(no_of_engines):
            engine = f.readline().strip()
            engines[j] = engine
        no_of_keywords = int(f.readline())
        keywords = no_of_keywords*[""]
        for k in range(no_of_keywords):
            keyword = f.readline().strip()
            keywords[k] = keyword
        #raw_input()
        answer = compute(engines,keywords)
        if answer == -1:
            answer = 0
        #print answer
        output_string = "Case #%s: %s" %(i+1,answer)
        print output_string
        #print engines,keywords
            
            
            
    


def main():
    f = open('/home/cslinux/Desktop/codejam/gcj/search/A-large.in','r')
    process_file(f)
main()

